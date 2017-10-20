/**
 * Created by 焦江龙 on 2017/3/31.
 */
$(document).ready(function() {
    $('.hadinfo').hover(
        function () {
            $('#hadinfo-ul').fadeIn();
        },
        function () {
            $('#hadinfo-ul').fadeOut();
        });

    $('#zhanghao').click(function(){
        $(this).addClass('on');
        $('.zhanghao').addClass('now');
        $('#tongzhi').removeClass('on');
        $('.tongzhi').removeClass('now');
        $('#bangding').removeClass('on');
        $('.bangding').removeClass('now');

    });
    $('#tongzhi').click(function(){
        $(this).addClass('on');
        $('.tongzhi').addClass('now');
        $('#zhanghao').removeClass('on');
        $('.zhanghao').removeClass('now');
        $('#bangding').removeClass('on');
        $('.bangding').removeClass('now');

    });
    $('#bangding').click(function(){
        $(this).addClass('on');
        $('.bangding').addClass('now');
        $('#zhanghao').removeClass('on');
        $('.zhanghao').removeClass('now');
        $('#tongzhi').removeClass('on');
        $('.tongzhi').removeClass('now');

    });
    $('#xingxi').click(function(){
        $(this).addClass('on');
        $('.form1').addClass('now1');
        $('#mima').removeClass('on');
        $('.form2').removeClass('now1');
        $('#youxiang').removeClass('on');
        $('.form3').removeClass('now1');

    });
    $('#mima').click(function(){
        $(this).addClass('on');
        $('.form2').addClass('now1');
        $('#xingxi').removeClass('on');
        $('.form1').removeClass('now1');
        $('#youxiang').removeClass('on');
        $('.form3').removeClass('now1');

    });
    $('#youxiang').click(function(){
        $(this).addClass('on');
        $('.form3').addClass('now1');
        $('#xingxi').removeClass('on');
        $('.form1').removeClass('now1');
        $('#mima').removeClass('on');
        $('.form2').removeClass('now1');

    });
});