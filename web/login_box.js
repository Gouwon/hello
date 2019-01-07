/* 제이쿼리 onload 확인 */
$( window ).on( "load", console.log('onload!!') );
$( document )
    .ready(function() 
    {
        console.log( "ready!" );
        $('#err').hide();
    })
;

function login_result() 
{   
    /* js
    var user_id = document.getElementById("user_id").value;
    var user_pw = document.getElementById("user_pw").value;
    */
    // jq
    var user_id = $("#user_id").val();
    var user_pw = $("#user_pw").val();

    if (user_id === "a" && user_pw === "1")
    {   
        /* js
        document.getElementById("form").style.display="none";
        document.getElementById("login_s").style.display="block";
        document.getElementById("login_f").style.display="none";
        */
        // jq
        $("#form").css("display", "none")
        $("#login_s").css("display", "block")
        $("#login_f").css("display", "none")
    }
    else
    {   
        /* js
        document.getElementById("form").style.display="block";
        document.getElementById("login_s").style.display="none";
        document.getElementById("login_f").style.display="block";
        */
       // jq
        var form = $("#form");
        var login_s = $("#login_s");
        var $login_f = $("#login_f"); // generally using $ meaning jq varables(object)

        form.show();
        login_s.hide();
        $login_f.show();
    }
    return false;
}

$('#getJson1')
    .on("click", function(evt) 
    {
        console.log("evt>>", evt);
        evt.preventDefault(); // 브라우저 기본 이벤트는 하지마!!
        evt.stopPropagation(); // 상위 이벤트는 수행하지마!
        getJson1();
    })
;

$('#getJson2')
    .on("click", function(evt) 
    {
        console.log("evt>>", evt);
        evt.preventDefault(); // 브라우저 기본 이벤트는 하지마!!
        evt.stopPropagation(); // 상위 이벤트는 수행하지마!
        getJson2();
    })
;

$('#getJson3')
    .on("click", function(evt) 
    {
        console.log("evt>>", evt);
        evt.preventDefault(); // 브라우저 기본 이벤트는 하지마!!
        evt.stopPropagation(); // 상위 이벤트는 수행하지마!
        getJson3();
    })
;

$('#ajax')
    .on("click", function(evt) 
    {
        console.log("evt>>", evt);
        evt.preventDefault(); // 브라우저 기본 이벤트는 하지마!!
        evt.stopPropagation(); // 상위 이벤트는 수행하지마!
        test_ajax();
    })
;

var URL = "http://berryservice.net:8080/Berry/g/tests/";

function getJson1() 
{
    $.get(URL)
        .then(function (json) 
        {
            var content = JSON.stringify(json, null, "  ");
            $("<h1>").text(json.test.length).appendTo("body");
            $("<pre class=\"content\">").html(content).appendTo("body");
        }, function (err) 
        {
            console.error("Sorry, there was a problem!", err.status, err);
        })
    ;
}

function getJson2() 
{
    $.ajax({url: URL,
            type: "GET",
            dataType: "json"})
        .done(function (json) 
        {
            var content = JSON.stringify(json, null, "  ");
            $("<pre class=\"content\">").html(content).appendTo("body");
        })
        .fail(function (xhr, status, errorThrown) 
        {
            console.error("Sorry, there was a problem!", err.status, err);
        })
        .always(function (xhr, status) 
        {
            console.log("The request is complete!");
        })
    ;
}

function getJson3() 
{
    $.get(URL)
        .always(function (xhr, status) 
        {
            console.log("The request is complete!", xhr, status);
            if (status === 'success') 
            {
                var content = JSON.stringify(xhr, null, "  ");
                console.log("cccccc>>", content)
                $("<h1>").text(xhr.test.length).appendTo("body");
                $("<pre class=\"content\">").html(content).appendTo("body");
            } 
            else 
            {
                console.log(">>>", xhr.responseText, xhr.status)
            }
        })
    ;
}


function test_ajax() 
{
    $.ajax({url: URL,
            type: "GET"})
        .done(function (json) 
        {
            var content = JSON.stringify(json, null, "  ");
            $("<pre class=\"content\">").html(content).appendTo("body");
        })
        .fail(function (xhr, status, errorThrown) 
        {
            // console.error("Sorry, there was a problem!", err.status, err);
            console.error("Error>>", xhr.responseJSON);
            var $err = $('#login_f');
            $err.text(xhr.responseJSON.message);
            $err.show();
        })
        .always(function (xhr, status) 
        {
            console.log("The request is complete!");
        })
    ;
}