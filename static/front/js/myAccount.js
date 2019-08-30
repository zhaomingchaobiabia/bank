$(function(){

 var li = $('ul.list_mi li a');

  li.eq(0).css('color','#f35d08').css('background','#fff');
 $.each(li,function(index,value){

     $(this).hover(function(){

        $(this).css('color','#f35d08').css('background','#fff');

        li.eq(0).css('color','#f35d08').css('background','#fff');

     },function(){

        $(this).css('color','#fff').css('background','#f7772c');

        li.eq(0).css('color','#f35d08').css('background','#fff');

     });



 });




var img = document.getElementById('img_list');
	
	var img1= img.children;
	
	for (var i=0;i<img1.length;i++) {
		
		img1[i].setAttribute('index',i);
		img1[0].onclick=function(){
			this.style.background='url(img/shouji.jpg) no-repeat';
			img1[2].style.background='url(img/shenfen.jpg) no-repeat';
			img1[1].style.background='url(img/youxiang.jpg) no-repeat';
		}
		img1[1].onclick=function(){
			this.style.background='url(img/youxi.jpg) no-repeat';
			img1[0].style.background='url(img/shou.jpg) no-repeat';
			img1[2].style.background='url(img/shenfen.jpg) no-repeat';
		}
		img1[2].onclick=function(){
			this.style.background='url(img/shenf.jpg) no-repeat';
			img1[0].style.background='url(img/shou.jpg) no-repeat';
			img1[1].style.background='url(img/youxiang.jpg) no-repeat';
		}
	
		
	}


	$("[type=file]").change(function(){
		var tag = $(this) ;
		var file = this.files[0] ;
		var fr = new FileReader();
		console.log(fr);
		fr.readAsDataURL(file);
		fr.onload = function(){
			tag.prev().find("img").attr('src' ,fr.result) ;
		}
		
	});

});
	










	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

