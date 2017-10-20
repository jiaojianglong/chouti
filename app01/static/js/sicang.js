
$(document).ready(function(){
    $('.hadinfo').hover(
            function(){
                $('#hadinfo-ul').fadeIn();
            },
            function(){
                $('#hadinfo-ul').fadeOut();
            });
    $('#fabu').click(function(){
        $(this).addClass('on');
        $('#sicang').removeClass('on');
        $('#pinglun').removeClass('on');
        $('#tuijian').removeClass('on');
        //var str = '';
        $.post('/fabu/',function(data,status){
            $('.content1').append(data);

             //$('#myTemplate').tmpl(data).appendTo('.content1');
            //$.each(data,function(n,value){
            //    var content = value.fields.content;
            //    var href = value.fields.href;
            //    var picture = value.fields.picture;
            //    var auther = value.fields.auther;
            //    var time = value.fields.time;
            //    var dianzan = value.fields.dianzan;

                //var main = $("<div class='content outer'><div class='text'></div></div>");
                //$('.content1').append(main);
                //var a = $('<a href="#" target="_blank"></a>').text(content);
                //a.attr('href',href);
                //main.append(a);
                //str +='<div class="content outer">'+
                //	'<div class="text">'+
                //		'<a href="'+href+'" target="_blank">'+content+'</a>'+
                //        '<span class="phone"></span>'+
                //        '<a href="#" class="from">图片</a>'+
                //        '<div class="shar">'+
                //        	'<a href="#">'+
                //            	'<span class="icon1 icon"></span>'+
                //                '<span class="b">'+dianzan+'</span>'+
                //           	 	'</a>'+
                //            	'<a href="#">'+
                //            		'<span class="icon2 icon"> </span>'+
                //                	'<span class="b">4</span>'+
                //            	'</a>'+
                //            	'<a href="#" >'+
                //            		'<span class="icon3 icon"> </span>'+
                //                	'<span class="b b3">私藏</span>'+
                //            	'</a>'+
                //            	'<a href="#">'+
                //         			'<img src="'+picture+'">'+
                //            		'<span class="b b4" >磨剪子磨菜刀军</span>'+
                //            	'</a>'+
                //            	'<a href="#" class="b5">'+
                //            		'<span>'+time+'</span>'+
                //                    '<span class="rebang">入热榜</span>'+
                //            	'</a>'+
                //        '</div>'+
                //    '</div>'+
                //    '<img class="img1" src="'+picture+'" />'+
                //    '<hr />'+
                //'</div>';

            //});

        });
        //$('.content1').append(str);
    });
});
