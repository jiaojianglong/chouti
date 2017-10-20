
function rebang(){
	var text1 = document.getElementById('text1');
	var text2 = document.getElementById('text2');
	var bang = document.getElementById('bang');
	var pinlun = document.getElementById('pinlun');
	text2.style.display = 'none';
	text1.style.display = 'block';
	bang.style.backgroundColor = '#4767b2';
	bang.style.color = '#fff';
	pinlun.style.backgroundColor = '#fff';
	pinlun.style.color = '#4767b2';
	}
//pinlun.addEventListener('click','repinlun',false);
function repinlun(){
	var text1 = document.getElementById('text1');
	var text2 = document.getElementById('text2');
	var bang = document.getElementById('bang');
	var pinlun = document.getElementById('pinlun');
	text1.style.display = 'none';
	text2.style.display = 'inline-block';
	pinlun.style.backgroundColor = '#4767b2';
	pinlun.style.color = '#fff';
	bang.style.backgroundColor = '#fff';
	bang.style.color = '#4767b2';
	}


$(document).ready(function(){
    $.post('/get_content/',function(data,status){
        $('#index_content').append(data);
    });


        $('#c-form1').click(function(){
            $('#form1').css('display','block');
            $(this).addClass('login-on');
            $('#c-form2').removeClass('login-on');
            $('#form2').css('display','none');
        });
        $('#c-form2').click(function(){
            $('#form2').css('display','block');
            $(this).addClass('login-on');
            $('#c-form1').removeClass('login-on');
            $('#form1').css('display','none');
        });
        $('.exit').mousemove(function(){
           $(this).css('background-position','0 -481px');
        })
        .mouseleave(function(){
           $(this).css('background-position','0 -499px');
        })
        .click(function(){
            $('#login').fadeOut();
        });
        $('#info').click(function(){
            $('#login').fadeIn();
        });
        $('#regest').click(function(){
            $('#login').fadeIn();
        });

        $('#form3-submit').click(function(){
            var address = $('#id_address3').val();
            var phone = $('#id_phone3').val();
            var pwd = $('#id_pwd3').val();
            $.post('/info1/',{address3:address,phone3:phone,pwd3:pwd},function(data,status){
                if(data=='error'){
                    var text = $('<span></span>').text('该手机号已经注册,请直接登录');
                    $('.errortishi').append(text);
                }
                else{
                    $('#first1').removeClass('on');
                    $('#second2').addClass('on');
                    $('.form3').css('display','none');
                    $('.form4').css('display','block');
                }

            });
            return false;
        });
        $('#form4-submit').click(function(){
            var name = $('#id_name4').val();
            var sex = $("input[name='sex']").val();
            var country = $('#id_country4').val();
            var province = $('#id_province4').val();
            var city = $('#id_city4').val();
            var content = $('#id_content4').val();
            $.post('/info2/', {sex4:sex,name4:name,country4:country,province4:province,city4:city,content4:content},function(data,status){
                if(data=='success'){
                    $('.login-success').fadeIn().fadeOut(3000);
                    $('#login').fadeOut(3000);
                }
                else{
                    $('#first1').removeClass('on');
                    $('#second2').addClass('on');
                    $('.form3').css('display','none');
                    $('.form4').css('display','block');
                }
                });
            return false;
        });
        $('#form12-submit').click(function(){
            var display = $('#form1').css('display');
            if(display == 'none'){
                var name = $('#id_name2').val();
                var pwd = $('#id_pwd2').val();
                $.post('/denglu2/',{name:name,pwd:pwd},function(data,status){
                    if(data=='log-success'){
                        $('.denglu-success').fadeIn().fadeOut(3000);
                        $('#login').fadeOut(3000);
                        location.reload(true);
                    }
                    else if(data=='name-error'){
                            var text1 =$('<span></span>').text('用户名错误');
                            $('#id_name2_error').append(text1);
                    }
                    else{
                        var text2 = $('<span></span>').text('密码错误');
                        $('#id_pwd2_error').append(text2)
                    }


                });

            }
            else{
                var address = $('#id_address1').val();
                var phone = $('#id_phone1').val();
                var pwd = $('#id_pwd1').val();
                $.post('/denglu1/',{address:address,phone:phone,pwd:pwd},function(data,status){
                   if(data=='success'){
                       $('.denglu-success').fadeIn().fadeOut(3000);
                        $('#login').fadeOut(3000);
                        location.reload(true);
                   }
                   else if(data=='phone-error'){
                            var text1 =$('<span></span>').text('手机号错误');
                            $('#id_phone1_error').append(text1);
                   }
                   else{
                        var text2 = $('<span></span>').text('密码错误');
                        $('#id_pwd1_error').append(text2)
                   }
                });
            }
            return false;
        });
    $('.hadinfo').hover(
            function(){
                $('#hadinfo-ul').fadeIn();
            },
            function(){
                $('#hadinfo-ul').fadeOut();
            });

});

