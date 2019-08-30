$(function(){
 
     //已注册用户，直接跳转到登陆页面
      var login_btn = $('.reg_mian form.reg_login p span.login');

      login_btn.click(function(){
          location.href="/front/login";
      });


    $(".login").prev().click(function () {
           var clic =  $(this);
           let che = $(":checkbox").prop("checked");
            if (flag && che && flag_1) {
                console.log(che);
                $("form").submit();
           }
        });


        <!-- 校验电话 -->
        var flag = false;
        $('[name=tel]').change(function () {
            var th = $(this);
            var tel =$(this).val();
            $.ajax({
                url:'/front/check',
                data: {"tel":tel},
                dataType:'json',
                method: 'post',
                async: true,
                success:function (data) {
                    if (data.tel===''){
                        let myreg=/^[1][3|4|5|7|8][0-9]{9}$/;
                        if (myreg.test(tel)){
                        th.next().attr('class', 'ok');
                        flag = true
                        }else {
                        th.next().attr('class', '');
                        flag = false
                            }
                    }else{
                        flag = false;
                        alert("该用户已注册");
                        th.val('')
                    }
                }

            });



        });

        <!-- 校验密码-->
        var flag_1 = false;
        $('[name=password]').change(function () {
            let regex = /^\w{6,16}$/;
            if (regex.test($(this).val())){
                let data =$(this).val();
                var da = $(this).next();
                da.attr('class', 'ok');
                var a = $('[name=pass]');
                if(data === a.val() ){
                    a.next().attr('class', 'ok');
                    flag_1 = true
                }
                else {
                    a.next().attr('class', '');
                    flag_1 = false
                }

            }else {
                $(this).next().attr('class', '');
                flag_1 = false
            }
        });
        <!-- 校验密码一致-->
        $('[name=pass]').change(function () {
            let regex = /^\w{6,16}$/;
            if ($(this).val() === $('[name=password]').val() && regex.test($(this).val())){
                $(this).next().attr('class', 'ok');
                flag_1 = true;
            }else {
                $(this).next().attr('class', '');
                flag_1 = false
            }
        });

        <!-- 校验验证码一致-->
        $('[name=security]').change(function () {
            if ($(this).val()){
                $(this).next().attr('class', 'ok')
            }else {
                $(this).next().attr('class', '');
                flag = false
            }
        });

});
