$(function(){
 
// 左侧列表
 var li = $('ul.list_mi li a');

  li.eq(1).css('color','#f35d08').css('background','#fff');
 $.each(li,function(index,value){

     $(this).hover(function(){

        $(this).css('color','#f35d08').css('background','#fff');

        li.eq(1).css('color','#f35d08').css('background','#fff');

     },function(){

        $(this).css('color','#fff').css('background','#f7772c');

        li.eq(1).css('color','#f35d08').css('background','#fff');

     });



 });

// tab切换栏

 var tab_li = $('.teble_tab ul li');
 tab_li.eq(0).css('color','#f7772c').css('borderBottom','none');
 $.each(tab_li,function(index,value){

     $(this).click(function(){

           $(this).css('color','#f7772c').css('borderBottom','none').siblings().css('color','#665d56').css('borderBottom','#e7e7e7 solid 1px');

     });

 });












});
