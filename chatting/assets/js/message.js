var csrftoken;
var last_primary_key = 0;
var selected_issue_name = '';
$(function() {
    $("#msg").keyup(function (e) {
        var regex = /#{2,}/;
        var input_valud = $("#msg").val();
        input_valud = autoLink(input_valud);
        var is_hashtag = regex.test(input_valud);
        if(is_hashtag) {
            $("#msg").val('#');
        }
        if (e.keyCode == 13 && $("#msg").val() != "") {
            send_message(input_valud);
        }
    });
    $("#btn_plus").click(function(){
        $("#popup_menu").toggle();
    });
    scroll_to_bottom('direct');
    setInterval(get_message, 3000);
});
function autoLink(content) {

    var regURL = new RegExp('(^|[^"])(http|https|ftp|telnet|news|irc)://([-/.a-zA-Z0-9_~#%$?&=:200-377()]+)', 'gi');

    var regURL2 = /(^|[^\/])(www\.[\S]+(\b|$))/gim;

    return content.replace(regURL, '$1<a class="autoLink" href="$2://$3" target="_blank">$2://$3</a>')

        .replace(regURL2, '$1<a class="autoLink" href="http://$2" target="_blank">$2</a>');
}



function scroll_to_bottom(mode){
    if(mode == 'smooth')
        $("html, body").animate({ scrollTop: $(document).height() }, "slow");
    else
        $('html, body').scrollTop( $(document).height() );
}
function get_message(){
    $.ajax({
        type: 'GET',
        contentType: 'application/json',
        url: '/message/get',
        data: {'last_primary_key': last_primary_key, 'issue_name': selected_issue_name },
        cache: false,
        success: function(response){
            append_messsage_to_div(response);
        },
        failure: function(response) {
            alert('sorry, load error. please try again');
        },
        complete:function(response){
            console.log(JSON.stringify(response));
        },
    });
}
function append_messsage_to_div(messages){
    $.each(messages, function(key){
        var username = messages[key].username;
        var time = messages[key].time;
        var content = messages[key].content;
        var file = messages[key].file;
        var message_tag = null;
        message_tag = '<div class="message"><div class="message_send_information"><span class="message_username">' + username + '</span><span class="message_time">' + time + '</span></div><div class="message_content">' + content + '</div></div>';
        $("#messages_container").append(message_tag);
        last_primary_key = messages[key].message_id;
        scroll_to_bottom('smooth');
        // In case of hash tag
        if(content.indexOf('#') != -1){
            var splited_string = content.split('#');
            splited_string = splited_string[1];
            splited_string = splited_string.split(" ");
            hash_tag = '<span class="message_hash_tag_name">' + '#'+ splited_string[0] + '</span>';
            $("#message_hash_container").append(hash_tag);
        }
    });
}
function send_message(msg){
    csrftoken = $("input[name*='csrfmiddlewaretoken']").val();
    $.ajax({
        type: 'POST',
        url: '/message/create',
        data: {content: msg, issue_name: selected_issue_name},
        cache: false,
        beforeSend:function(xhr){
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function(response) {
            if(response == "insert_success")
                get_message();
        },
        failure: function(response) {
            alert('sorry, insert error. please try again');
        },
        complete: function(response){
            console.log(JSON.stringify(response));
            $("#msg").val("");
        },
    });
}
