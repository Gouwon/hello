db.test.drop()

use testdb
db
show dbs

/*
 *
 * 아래와 같이 100개의 가수 문서를 만드시오.
 * {name: 'singer1', company: 'comp1', likecnt: 1},
 * {name: 'singer2', company: 'comp2', likecnt: 1}, …
 *
 */
 for (var i = 0; i < 100; i++) {
    db.test.insert({"name" : "singer" + (i + 1), "company" : "comp" + (i + 1), "likecnt" : 1})
 };
 
db.test.find();


 /*
  *
  * singer1의 문서에 albums 키를 추가하시오.(변수 사용 - save())
  * albums = [1, 2, 3]
  *
  */
  

var singer1 = db.test.findOne({"name" : "singer1"})

singer1.album = [1, 2, 3]


db.test.save(singer1)

db.test.findOne({"name" : "singer1"})


/*
 *
 *singer1의 문서에 아래 노래(hitsongs) 2곡을 추가하시오.($set 사용)
 *
 */
 
db.test.update( {"name":"singer1"}, 
				{ $set: { "hitsongs" : [{title: '24/7', albumId: 1},
                                        {title: '222', albumId: 2}] } 
			     }
                )
var singer1 = db.test.findOne({"name" : "singer1"})
db.test.save(singer1)
db.test.findOne({"name" : "singer1"})

/*
 *
 * singer1의 likecnt를 제거하시오. ($unset 사용)
 *
 */
 
db.test.update( {"name":"singer1"}, 
				{ 
			    	$unset: {"likecnt" : 1 } 
			     }
                )
var singer1 = db.test.findOne({"name" : "singer1"})
db.test.save(singer1)
db.test.findOne({"name" : "singer1"})           



/*
 *
 * Singer collection의 singer3에 albums에 10을 push 하시오.
 *
 */
 

db.test.findOne({"name" : "singer3"})
var s3 = db.text.findOne({"name" : "singer3"})
db.test.update({"name" : "singer3"},
                {$push: {"album" : 10}})
db.test.findOne({"name" : "singer3"})

/*
 *
 * singer4의 albums에 100 ~ 110 까지 $each를 사용하여 push하시오.
 *
 */


db.test.findOne({"name" : "singer4"});
var lst = new Array();
for (var i = 0; i < 11; i++){
    lst[i] = i + 100;
}
db.test.update({"name" : "singer4"}, 
                {$push : { "album" : {$each : lst})
db.test.findOne({"name" : "singer4"});


/*
 *
 * singer4의 albums에 105번을 제거하시오.
 *
 */
 
db.test.findOne({"name" : "singer4"});
db.test.update({"name" : "singer4"}, 
                {$pull : {"album" : 105}});
var s4 = db.test.findOne({"name" : "singer4"});
db.test.findOne({"name" : "singer4"});



/*
 *
 * Singer collection의 singer1 ~ singer10 가수에 대해 likecnt가 존재하면 1증가 하고, 없으면 1로 초기화 하시오.
 *
 */
 
var lst = [];
for (var i = 0; i < 10; i++) {
    lst[i] = "singer" + (i + 1)
}
 
db.test.update( {"name" : {$in : lst}}, 
				 {$inc: {likecnt: 1} },
				 true, 
				 true
                )

for (var i = 0; i < 10; i++) {
 db.test.update({"name" : "singer" + (i + 1)}, 
                {$inc : {"likecnt" : 1}}, 
                true
                )   
}    

db.test.find();

/*
 *
 * Singer collection의 likecnt=1인 문서 전체를 likecnt++ 하시오.
 *
 */
 
db.test.update( {"likecnt" : 1}, 
				 {$inc: {likecnt: 1} },
				 true, 
				 true
                );

db.test.find();


/*
 *
 *
 *
 */
 
db.food.insert({ _id: 1, fruit: ['apple', 'banana', 'peach'] });
db.food.insert({ _id: 2, fruit: ['apple', 'orange', 'melon'] });
db.food.insert({ _id: 3, fruit: ['cherry', 'peach'] });

db.food.find();

db.food.find({ fruit: { $all: ['apple', 'banana'] } });
db.food.find({ fruit: { $in: ['apple', 'banana'] } });


/*
 *
 *  Song collection을 cursor를 이용하여, 5번째, 10번째, 15번째… 의 likecnt를 10으로 수정하시오.
 *
 */

db.test.find();

var cur = db.test.find();
while ( cur.hasNext() ) {
    for (var i = 1; i < 101; i++) {
        if ( i % 5 === 0) {
            db.test.update({"name" : "singer" + i}, {$set : {"likecnt" : 10}})
            db.test.save({"name" : "singer" + i})
        }
    }
}


var cur = db.test.find();
var i = 0;
while( cur.hasNext() ){
    i++;
    var s = cur.next();
    if ( i % 5 !== 0 ) continue;
    s.likecnt = 10;
    db.test.save(s);
}

var cur = db.test.find();
var i = 0;
cur.forEach((s)=> { 
    i++;
    if ( i % 5 === 0 ) {
       s.likecnt = 10;
       db.test.save(s);
    }
});

db.test.find({"likecnt" : 10});

/*
 *
 *  수정된 document중 5개만 출력하시오.(출력 키: name, likecnt)
 *
 */
 
db.test.find({}, {_id : 0, "name" : 1, "likecnt" : 1}).sort({"likecnt" : -1}).limit(5)