$(function(){
    var team;
    var user;
    function update_user(users) {
        $.each(users, function(key){
            var username = users[key].user;
            var ul_tag = '<li id=' +username+ '><a role="menuitem" tabindex="-1">' + username + '</a></li>';
            $("#ul_users").append(ul_tag);
        });
    }
    $('#ul_my_teams').on("click", 'li', function (event) {
        team = $(event.target).text();
        $('#my_teams_title').text(team);
        get_users(team);
    });
    $('#ul_users').on("click", 'li', function (event) {
        user = $(event.target).text();
        $('#add_user_title').text(user);
    });
    $('#btn_invite_submit').click(function(){
        if(team != null && user != null) {
            $('#create-invite-modal').modal('hide')
            invite_user(team, user);
        }
        else {
            alert("Select item");
        }
    });
    function get_users(team){
        csrftoken = $("input[name*='csrfmiddlewaretoken']").val();

        $.ajax({
            type: 'POST',
            url: '/team/get_users',
            data: {team: team},
            cache: false,
            beforeSend:function(xhr){
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            success: function(response) {
                update_user(response);
            },
            failure: function(response) {
                alert('sorry, insert error. please try again');
            },
            complete: function(response){
                console.log(JSON.stringify(response));
            },
        });
    }
    function invite_user(team, user){
        csrftoken = $("input[name*='csrfmiddlewaretoken']").val();

        $.ajax({
            type: 'POST',
            url: '/team/invite',
            data: {team: team, user: user},
            cache: false,
            beforeSend:function(xhr){
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            success: function(response) {
                alert('success');
            },
            failure: function(response) {
                alert('sorry, insert error. please try again');
            },
            complete: function(response){
                console.log(JSON.stringify(response));
            },
        });
    }
});
