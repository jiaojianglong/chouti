/**
 * Created by 焦江龙 on 2017/4/4.
 */
$(document).ready(function(){
    $('.a_dianzhan').click(function(){
        var icon = $(this).children('.icon1');
        if(icon.css('background-position')=='0px -40px'){
            var id1 = $(this).children('.share_id').text();
            var obj = $(this);
            $.post('/add_sicang/', {'id': id1}, function (data, status) {
                //转换为json对象
                var dict = jQuery.parseJSON(data);
                if (dict['sta'] == 'success') {
                    var icon = obj.children('.icon1');
                    icon.css('background-position', '0 -20px');
                    var num = dict['num'];
                    var text = obj.children('.b');
                    text.text(num);
                }
                else {

                }
            });
        }
        else{}
    return false;
    });
});
