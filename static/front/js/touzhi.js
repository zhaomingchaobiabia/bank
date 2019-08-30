$(function(){
 
/***************投资填写弹窗*******************/

  var mstz_btn = $('.mstz');
  var dialog = $('.dialog');
  var close_btn = $('.dialog .content_right .close');

  mstz_btn.click(function(){

  	dialog.show();
  });

 close_btn.click(function(){

  	dialog.hide();
  });


/***************TAB切换栏*******************/


var tz_tab_li = $('.tz_tab ul li');
var tz_tab_content = $('.tz_tab .tz_tab_content>div');

tz_tab_li.eq(0).attr('class','active');
tz_tab_content.eq(0).show();


$.each(tz_tab_li,function(index,value){

   $(this).click(function(){


         $(this).addClass('active').siblings().removeClass('active');
         tz_tab_content.eq(index).show().siblings().hide();
   });
});
});

$(function () {
    $('#cz').click(function () {
        location.href = '/account_management/money_record/'
    })
});

$(function () {
    $('#more').click(function () {
        location.href = '/front'
    })
});

$(function () {
    $('#tbm').change(function () {
        let money = $(this).val();
        $.ajax({
            url:'/property/tbmoney',
            data:{'tbm':money},
            method:'GET',
            dataType: 'json',
            success:function (data) {
                alert(data.msg);
            }
        })
    })
});

$(function () {
    $('#toubiao').click(function () {
        $(this).parents('form').submit()
    })
});

	// function time()
			// {
			// 	var date=new Date()
			// 	var year=date.getFullYear()
			// 	var month=date.getMonth()
			// 	var day=date.getDate()
			// 	var hour=date.getHours()
			// 	var minu=date.getMinutes()
			// 	var second=date.getSeconds()
			// 	console.info(year+"-"+month+"-"+day+"  "+hour+":"+minu+":"+second)
			// 	var time=year+"-"+month+"-"+day+"  "+hour+":"+minu+":"+second
			// 	document.getElementById("bb").innerHTML=time
			// }






function time2() {
    if(k==0) {
        k=2;
        day=6;
         hour=23;
         minu=53;
         second=16
    }
    second--;
    if(second==0) {
        second=60;
        minu--;
        if(minu==0)
            {
            minu=60;
            hour--;
            if(hour==0) {
                    hour=24;
                    day=day-1;
                    if(day==0){
                        // clearInterval()
                    }
                }
            }
    }


    var time= '可投时间：<span>'+day+'</span>天<span>'+hour+'</span>时<span>'+minu+'</span>分<span>'+second+'</span>秒';
    document.getElementById("timed").innerHTML=time


}

k=0;

var id=setInterval("time2()",1000);