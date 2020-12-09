from datetime import datetime
import sqlite3
import wx
import wx.html2  # WebView
import ntpath  # 파일 이름 추출
import base64  # 이미지 URI 인코딩

RECORD_PER_PAGE = 5


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
                          title='140자 일기장', size=wx.Size(715, 655), style=wx.DEFAULT_FRAME_STYLE
                          )
        # 미리보기 이미지의 크기가 가로 / 세로 최대 200 픽셀을 넘지 앟도록 설정하는 변수를 정의합니다.
        self.MaxImageSize = 200
        self.mainPanel = wx.Panel(self)

        # 일기 입력창
        self.leftPanel = wx.Panel(self.mainPanel)
        self.leftPanel.SetMaxSize(wx.Size(200, -1))
        self.input_image_path = ''
        # TextCtrl 위젯의 style에 wx.TE_MULTILINE을 지정하면 '\n'을 줄바꿈으로 표시할 수 있습니다.
        self.inputTextCtrl = wx.TextCtrl(self.leftPanel, size=wx.Size(200, 100), style=wx.TE_MULTILINE)
        # 일기 텍스트를 입력받는 위젯의 최대 텍스트 길이는 140입니다.
        self.inputTextCtrl.SetMaxLength(140)
        self.inputTextCtrl.Bind(wx.EVT_TEXT, self.OnTypeText)
        self.lengthStaticText = wx.StaticText(self.leftPanel, style=wx.ALIGN_RIGHT)
        self.selectImageButton = wx.Button(self.leftPanel, label='이미지 추가')
        self.selectImageButton.Bind(wx.EVT_BUTTON, self.OnFindImageFile)
        self.imageStaticBitmap = wx.StaticBitmap(self.leftPanel)
        self.inputButton = wx.Button(self.leftPanel, label='저장')
        self.inputButton.Bind(wx.EVT_BUTTON, self.OnInputButton)

        # 일기 표시창
        self.rightPanel = wx.Panel(self.mainPanel)
        self.outputHtmlWnd = wx.html2.WebView.New(self.rightPanel)
        # 일기 내용을 표시한 WebView 객체를 정의합니다.
        self.outputHtmlWnd.Bind(wx.html2.EVT_WEBVIEW_NAVIGATING, self.OnNavigating)

        # 위젯 배치
        leftPanelSizer = wx.StaticBoxSizer(wx.VERTICAL, self.leftPanel, '글 남기기')
        leftPanelSizer.Add(self.inputTextCtrl, 0, wx.ALL, 5)
        leftPanelSizer.Add(self.lengthStaticText, 0, wx.ALIGN_RIGHT | wx.RIGHT, 5)
        leftPanelSizer.Add(self.selectImageButton, 0, wx.ALIGN_RIGHT | wx.RIGHT, 5)
        leftPanelSizer.Add(self.imageStaticBitmap, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        leftPanelSizer.Add(self.inputButton, 0, wx.ALIGN_RIGHT | wx.RIGHT, 5)
        self.leftPanel.SetSizer(leftPanelSizer)

        htmlWndSizer = wx.GridSizer(1, 1, 0, 0)
        htmlWndSizer.Add(self.outputHtmlWnd, 0, wx.ALL | wx.EXPAND, 5)

        self.rightPanel.SetSizer(htmlWndSizer)
        self.rightPanel.Layout()
        htmlWndSizer.Fit(self.rightPanel)

        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        # QQQQQQQQQQQQQQQQQQQ
        # mainSizer.Add(self.leftPanel, 1, wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5)
        ## wx._core.wxAssertionError: C++ assertion "!(flags & wxALIGN_RIGHT)" failed at ..\..\src\common\sizer.cpp(2168) in wxBoxSizer::DoInsert(): Horizontal alignment flags are ignored in horizontal sizers
        mainSizer.Add(self.leftPanel, 1, wx.ALL | wx.EXPAND, 5)
        mainSizer.Add(self.rightPanel, 1, wx.ALL | wx.EXPAND, 5)
        self.mainPanel.SetSizer(mainSizer)
        self.Layout()

        # Database 초기화
        # 140자 일기장에서 사용할 데이터베이스 파일 이름은 minutediary.db입니다.
        self.conn = sqlite3.connect('minutediary.db')
        self.cursor = self.conn.cursor()
        # CheckSchema() 메소드는 minutediary.db에 스키마를 생성하고, LoadDiary() 메소드는 데이터베이스에서 레코드를 불러 WebView에 그 내용을 출력합니다.
        self.CheckSchema()
        self.LoadDiary(0)

    def CheckSchema(self):
        self.cursor.execute("""
                            create table if not exists diary (
                                diary_id integer primary key autoincrement, 
                                createdate datetime, 
                                note char(140))
                            """
                            )

        self.cursor.execute("""
                            create table if not exists diary_img (
                                img_id integer primary key autoincrement,
                                img blob, 
                                diary_id integer,
                                foreign key(diary_id) references diary(diary_id))
                            """
                            )

    def OnTypeText(self, event):
        self.lengthStaticText.SetLabel('현재 글자 수: {0}'.format(len(self.inputTextCtrl.GetValue())))
        # lengthStaticText의 표시 텍스트가 달라지면 위젯의 크기도 변합니다. 컨테이너 위젯의 Layout() 메소드를 호출해서 위젯을 재배치합니다.
        self.leftPanel.Layout()

    def OnFindImageFile(self, event):
        # wx.FileDialog의 인스턴스를 생성합니다.
        openFileDialog = wx.FileDialog(self, 'Open',
                                       wildcard='Image files (*.png, *.jpg, *.gif)|*.png;*.jpg;*.jpeg;*.gif',
                                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
                                       )

        if openFileDialog.ShowModal() == wx.ID_OK:
            self.input_image_path = openFileDialog.GetPath()

            # 비율을 유지하면서 이미지 크기를 윈도우에 맞추기
            # openFileDialog를 통해 얻어온 이미지 파일을 wx.Image 객체를 통해 엽니다.
            img = wx.Image(self.input_image_path, wx.BITMAP_TYPE_ANY)
            Width = img.GetWidth()
            Height = img.GetHeight()

            if Width > Height:
                NewWidth = self.MaxImageSize
                NewHeight = self.MaxImageSize * Height / Width
            else:
                NewWidth = self.MaxImageSize
                NewHeight = self.MaxImageSize * Height / Width

            # Scale() 메소드를 통해 Image 객체의 크기를 조정합니다.
            img = img.Scale(NewWidth, NewHeight)
            # imageStaticBitmap에 크기가 조정된 이미지 객체를 지정합니다.
            # QQQQQQQQQQQQQQQQQQQ
            self.imagestaticBitmap.SetBitmap(wx.Bitmap())
            self.leftPanel.Layout()
            self.leftPanel.Refresh()

    def OnInputButton(self, event):
        fileName = ntpath.basename(self.input_image_path)
        # DIARY 테이블에 레코드를 추가합니다.
        self.cursor.execute("""insert into diary (diary_id, createdate, note) values(null, ?, ?)""",
                            (str(datetime.now()), self.inputTextCtrl.GetValue()))

        # DIARY 테이블에 추가된 레코드의 DIARY_ID를 얻어옵니다.
        diary_id = self.cursor.lastrowid

        if self.input_image_path.strip() != "":
            # DIARY_IMG 테이블에 레코드를 추가합니다.
            self.cursor.execute("""insert into diary_img(img_id, img, diary_id) values(null, ?, ?)""",
                                (sqlite3.Binary(open(self.input_image_path, 'rb').read()), diary_id))

        self.conn.commit()

        wx.MessageBox('저장되었습니다.', '140자 일기장', wx.OK)

        # 데이터베이스에 일기 내용을 입력한 후에는 변수와 위젯을 초기화합니다.
        self.inputTextCtrl.SetValue('')
        self.ipnut_image_path = ''
        self.imageStaticBitmap.SetBitmap(wx.Bitmap(0, 0))

        self.leftPanel.Layout()
        self.leftPanel.Refresh()
        # 레코드 입력 후에는 LoadDiary() 메소드를 호출해서 사용자에게 일기 내용을 보여줍니다.
        self.LoadDiary(0)

    def LoadDiary(self, page):
        # 이 select문은 outer join을 이용해서 두 테이블에서 diary_id가 같은 레코드를 조회하여 하나의 결과로 만듭니다.
        # limit은 c최대 조회 건 수, offset은 읽어 들일 레코드의 순서를 지정합니다.
        self.cursor.execute("""
                            select d.diary_id, d.createdate, d.note, i.img 
                            from diary as d left outer join diary_img as i on d.diary_id = i.diary_id 
                            order by d.createdate desc limit {0} offset {1}
                            """.format(RECORD_PER_PAGE, page * RECORD_PER_PAGE)
                            )

        html = """<html>
                    <head>
                    </head>
                    <body>
                    {0}
                    </body>
                </html>    
            """

        diary_id = 0
        body = ""

        for row in self.cursor:
            dirary_id = int(row[0])
            imgTag = ''
            if row[3]:
                imgTag = """<img src='data:image/pang:base64,{0}' 
                                style='width:300px; height:auto;' 
                                align=center>""".format(base64.b64encode(row[3]).decode('ascii')
                                                        )

                # 삭제 링크에 diary_id를 지정합니다. [삭제] 버튼의 하이퍼링크 주소는 'del:'로 시작합니다.
                content = """<a name='neural'>
                                <p style='word-wrap:break-word;font-size=12px;'>
                                    <font size=2>
                                        <b>
                                            <i>
                                                {1}
                                            </i>
                                        </b>
                                        <a href='del:{0}'>[삭제]</a>
                                    </font>
                                    <br>
                                    {2}
                                    <br>
                                    {3}
                """.format(diary_id, row[1], row[2], imgTag)
                body += content

        pageNavigation = "<p align='center' style='font-size=12px'>"

        # Prev 버튼(링크)
        # 이전 페이지를 불러오는 버튼을 만듭니다. [Prev] 버튼의 하이퍼링크의 주소는 'nav:'로 시작합니다.
        if page > 0:
            pageNavigation += "<a href='nav:{0}'>Prev</a>".format(page - 1)

        pageNavigation += '&nbsp;'

        # Next 버튼(링크)
        # count(*)는 레코드의수를 세는 SQL 함수입니다.
        self.cursor.execute("""select count(*) from diary where diary_id<{0}""".format(diary_id))
        row = self.cursor.fetchone()

        if row:
            nextRowCount = row[0]
            # 다음 페이지를 불러오는 버튼을 만듭니다. [Next] 버튼의 하이퍼링크의 주소는 'nav:'로 시작합니다.
            if nextRowCount > 0:
                pageNavigation += "<a href='nav:{0}'>Next</a>".format(page + 1)

        pageNavigation += "</p>"
        body += pageNavigation

        # WebView 위젯에 최종적으로 완성된 HTML 텍스트를 입력합니다.
        self.outputHtmlWnd.SetPage(html.format(body), '')

    def OnNavigating(self, event):
        # event.URL이 'del'로 시작하면 delete문을 실행합니다. 이 delete문은 옆에 붙어 있는 diary_id에 해당하는 레코드를 삭제합니다.
        if event.URL.startswith('del:') == True:
            diary_id = event.URL.rpartition(':')[-1]
            self.cursor.execute('delete from diary where diary_id = {0}'.format(diary_id))
            self.cursor.execute('delete from diary_img where diary_id ={0}'.format(diary_id))
            self.conn.commit()
            self.LoadDiary(0)
            wx.MessageBox('삭제했습니다.', '140자 일기장', wx.OK)
        elif event.URL.startswith('nav:') == True:
            # event.URL이 'nav:'로 시작하면 LoadDiary() 메소드를 호출합니다. 이 때 'nav:' 뒤에 있는 페이지 번호를 떼어내어 LoadDiary()에 매개변수로 넘깁니다.
            page = event.URL.rparition(':')[-1]
            self.LoadDiary(int(page))

        # WebView  위젯이 해당 이벤트를 받아서 해당 URL로 이동하려는 것을 막기 위한 것입니다.
        event.Skip(False)


if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    frame.Show()

    app.MainLoop()
