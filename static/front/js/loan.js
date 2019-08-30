$(function () {
     $('.sub').click(function (){
         let name= $('[name=realname]').val();
         let tel = $('[name=tel]').val();
         let region = $('[name=region]').val();
         let money = $("[name=money]").val();
         let loan = $('[name=loan]').val();
         let loantype = $('[name=loantype]').val();
         let loanuse = $('[name=loanuse]').val();
         console.log(name,tel);
       $.ajax({
           url: '/property/borrow_screen',
           data:{'name':name,'tel':tel,'region':region,'money':money,'loan':loan,"loantype":loantype,'loanuse':loanuse},
           type:'GET',
           dataType:'json',
           success:function (data) {
               alert(data.msg);
           }
       })
     });
});
