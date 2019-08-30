$(function(){
    $(".middle_2_2 span").click(function () {
            var htm = $(this);
            var data2=htm.attr('id');
            console.log(data2);
            var data3 = $('.middle_2_3 .spanbb').find('span').attr('id');
            var data4 = $('.middle_2_4 .spanbb').find('span').attr('id');
            var data5 = $('.middle_2_5 .spanbb').find('span').attr('id');
            $('.middle_2_2 span').parent().attr('class','');
            console.log(data3);
            console.log(data4);
            console.log(data5);
            htm.parent().attr('class','spanbb');
            $.ajax({
                url: '/front/index_show',
                data: {"data2":data2,'data3':data3, 'data4':data4,'data5':data5},
                dataType: 'json',
                method: 'post',
                async: true,
                success: function (data) {
                        console.log(data);
                        var htm='';
                        for (var i = 0; i<data.data.length; i++){
                            if(i>4){
                                break
                            }
                            var user = data.data[i];
                            htm +=`
                                        <div class="middle_3">
                                    <div class="middle_3_1 title">
                                        <span class="middle_3_1_span">`+user.project_name +`</span>
                                        <img src="/static/front/img/hot.jpg"/>
                                    </div>
                                    <ul class="middle_3_2">
                                        <li>
                                            <p>预期年化利率</p>
                                            <span class="middle_3_2_span">`+ user.rate +`%</span>
            
                                        </li>
                                        <li>
                                            <p>投资期限</p>
                                            <span>`+ user.loan +`个月</span>
                                        </li>
                                        <li>
                                            <p>还款方式</p>
                                            <span>`+ user.repay_type +`</span>
                                        </li>
                                        <li>
                                            <p>项目总额</p>
                                            <span>`+ user.money +`元</span>
                                        </li>
            
                                    </ul>
            
                                    <div class="box">
                                        `+ user.rate +`%
                                    </div>`;
                    if(user.status === '筹资中'){
                                       htm += `<div class="middle_3_3">
                                        <a href="/property/touzhi?id=`+ user.id+`">我要投资</a>
                                    </div>
                                </div>`}
                    else if (user.status ==='已完成'){
                         htm+=`<div class="middle_3_3_1">
                                     已完成
                                    </div>
                                </div>`}

                    else{
                                htm+=`<div class="middle_3_3_1">
                                     已结束
                                    </div>
                                </div>`}
                        }

                    $('.middle_show').html(htm)
                }

            });
    });
    $(".middle_2_4 span").click(function () {
                      var htm = $(this);
            var data4=htm.attr('id');
            console.log(data2);
            var data3 = $('.middle_2_3 .spanbb').find('span').attr('id');
            var data2 = $('.middle_2_2 .spanbb').find('span').attr('id');
            var data5 = $('.middle_2_5 .spanbb').find('span').attr('id');
            $('.middle_2_4 span').parent().attr('class','');
            console.log(data3);
            console.log(data4);
            console.log(data5);
            htm.parent().attr('class','spanbb');
            $.ajax({
                url: '/front/index_show',
                data: {"data2":data2,'data3':data3, 'data4':data4,'data5':data5},
                dataType: 'json',
                method: 'post',
                async: true,
                success: function (data) {
                        console.log(data);
                        var htm='';
                        for (var i = 0; i<data.data.length; i++){
                            if(i>4){
                                break
                            }
                            var user = data.data[i];
                            htm +=`
                                        <div class="middle_3">
                                    <div class="middle_3_1 title">
                                        <span class="middle_3_1_span">`+user.project_name +`</span>
                                        <img src="/static/front/img/hot.jpg"/>
                                    </div>
                                    <ul class="middle_3_2">
                                        <li>
                                            <p>预期年化利率</p>
                                            <span class="middle_3_2_span">`+ user.rate +`%</span>
            
                                        </li>
                                        <li>
                                            <p>投资期限</p>
                                            <span>`+ user.loan +`个月</span>
                                        </li>
                                        <li>
                                            <p>还款方式</p>
                                            <span>`+ user.repay_type +`</span>
                                        </li>
                                        <li>
                                            <p>项目总额</p>
                                            <span>`+ user.money +`元</span>
                                        </li>
            
                                    </ul>
            
                                    <div class="box">
                                        `+ user.rate +`%
                                    </div>`;
                    if(user.status === '筹资中'){
                                       htm += `<div class="middle_3_3">
                                      <a href="/property/touzhi?id=`+ user.id +`">我要投资</a>
                                    </div>
                                </div>`}
                    else if (user.status ==='已完成'){
                         htm+=`<div class="middle_3_3_1">
                                     已完成
                                    </div>
                                </div>`}

                    else{
                                htm+=`<div class="middle_3_3_1">
                                     已结束
                                    </div>
                                </div>`}
                        }

                    $('.middle_show').html(htm)
                }

            });
    });
    $(".middle_2_3 span").click(function () {
                      var htm = $(this);
            var data3=htm.attr('id');
            console.log(data2);
            var data2 = $('.middle_2_2 .spanbb').find('span').attr('id');
            var data4 = $('.middle_2_4 .spanbb').find('span').attr('id');
            var data5 = $('.middle_2_5 .spanbb').find('span').attr('id');
            $('.middle_2_3 span').parent().attr('class','');
            console.log(data3);
            console.log(data4);
            console.log(data5);
            htm.parent().attr('class','spanbb');
            $.ajax({
                url: '/front/index_show',
                data: {"data2":data2,'data3':data3, 'data4':data4,'data5':data5},
                dataType: 'json',
                method: 'post',
                async: true,
                success: function (data) {
                        console.log(data);
                        var htm='';
                        for (var i = 0; i<data.data.length; i++){
                            if(i>4){
                                break
                            }
                            var user = data.data[i];
                            htm +=`
                                        <div class="middle_3">
                                    <div class="middle_3_1 title">
                                        <span class="middle_3_1_span">`+user.project_name +`</span>
                                        <img src="/static/front/img/hot.jpg"/>
                                    </div>
                                    <ul class="middle_3_2">
                                        <li>
                                            <p>预期年化利率</p>
                                            <span class="middle_3_2_span">`+ user.rate +`%</span>
            
                                        </li>
                                        <li>
                                            <p>投资期限</p>
                                            <span>`+ user.loan +`个月</span>
                                        </li>
                                        <li>
                                            <p>还款方式</p>
                                            <span>`+ user.repay_type +`</span>
                                        </li>
                                        <li>
                                            <p>项目总额</p>
                                            <span>`+ user.money +`元</span>
                                        </li>
            
                                    </ul>
            
                                    <div class="box">
                                        `+ user.rate +`%
                                    </div>`;
                    if(user.status === '筹资中'){
                                       htm += `<div class="middle_3_3">
                                        <a href="/property/touzhi?id=`+ user.id+`">我要投资</a>
                                    </div>
                                </div>`}
                    else if (user.status ==='已完成'){
                         htm+=`<div class="middle_3_3_1">
                                     已完成
                                    </div>
                                </div>`}

                    else{
                                htm+=`<div class="middle_3_3_1">
                                     已结束
                                    </div>
                                </div>`}
                        }

                    $('.middle_show').html(htm)
                }

            });
    });
    $(".middle_2_5 span").click(function () {
                       var htm = $(this);
            var data5=htm.attr('id');
            console.log(data2);
            var data3 = $('.middle_2_3 .spanbb').find('span').attr('id');
            var data4 = $('.middle_2_4 .spanbb').find('span').attr('id');
            var data2 = $('.middle_2_2 .spanbb').find('span').attr('id');
            $('.middle_2_5 span').parent().attr('class','');
            console.log(data3);
            console.log(data4);
            console.log(data5);
            htm.parent().attr('class','spanbb');
            $.ajax({
                url: '/front/index_show',
                data: {"data2":data2,'data3':data3, 'data4':data4,'data5':data5},
                dataType: 'json',
                method: 'post',
                async: true,
                success: function (data) {
                        console.log(data);
                        var htm='';
                        for (var i = 0; i<data.data.length; i++){
                            if(i>4){
                                break
                            }
                            var user = data.data[i];
                            htm +=`
                                        <div class="middle_3">
                                    <div class="middle_3_1 title">
                                        <span class="middle_3_1_span">`+user.project_name +`</span>
                                        <img src="/static/front/img/hot.jpg"/>
                                    </div>
                                    <ul class="middle_3_2">
                                        <li>
                                            <p>预期年化利率</p>
                                            <span class="middle_3_2_span">`+ user.rate +`%</span>
            
                                        </li>
                                        <li>
                                            <p>投资期限</p>
                                            <span>`+ user.loan +`个月</span>
                                        </li>
                                        <li>
                                            <p>还款方式</p>
                                            <span>`+ user.repay_type +`</span>
                                        </li>
                                        <li>
                                            <p>项目总额</p>
                                            <span>`+ user.money +`元</span>
                                        </li>
            
                                    </ul>
            
                                    <div class="box">
                                        `+ user.rate +`%
                                    </div>`;
                    if(user.status === '筹资中'){
                                       htm += `<div class="middle_3_3">
                                       <a href="/property/touzhi?id=`+ user.id+`">我要投资</a>
                                    </div>
                                </div>`}
                    else if (user.status ==='已完成'){
                         htm+=`<div class="middle_3_3_1">
                                     已完成
                                    </div>
                                </div>`}

                    else{
                                htm+=`<div class="middle_3_3_1">
                                     已结束
                                    </div>
                                </div>`}
                        }

                    $('.middle_show').html(htm)
                }

            });
    });
});
