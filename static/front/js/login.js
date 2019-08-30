$(function () {
                $('[name=name]').change(function () {
                    var th = $(this);
                    var a = $(this).val();
                    $.ajax({url: '/front/login_name',
                            data: {"data":a,csrfmiddlewaretoken:'{{csrf_token}}'},
                            method: 'post',
                            dataType: "json",
                            async: true,
                            success: function (data) {
                            console.log(data);
                                if(data.data!==''){
                                    alert(data.data);
                                    th.val('')
                                }
                            }
                    })
                });


                $("form a").click(function () {
                    $('form').submit()
                });

             //没有账号用户，直接跳转到注册页面
              var login_btn = $('.reg_span');

              login_btn.click(function(){
                  location.href="/front/reg";
              });
            });