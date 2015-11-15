$(function(){
    $('#create-setting-modal').on('shown.bs.modal', function() {
        var assignment;
        var status;
        var issue;
        $('#ul_issues').on("click", 'li', function (event) {
            issue = $(event.target).text();
            $('#select_issue_title').text(issue);
        });
        $('#ul_assignment').on("click", 'li', function (event) {
            assignment = $(event.target).text();
            $('#assignment_title').text(assignment);
        });
        $('#ul_status').on("click", 'li', function (event) {
            status = $(event.target).text();
            $('#status_title').text(status);
        });
        $('#btn_change_status_submit').click(function(){
            if(assignment != null && status != null && issue != null) {
                $('#create-setting-modal').modal('hide')
                change_status(assignment, status, issue);
            }
            else {
                alert("Select item")
            }
        });
    })
});
        function change_status(assignment, status, issue){
            csrftoken = $("input[name*='csrfmiddlewaretoken']").val();

            $.ajax({
                type: 'POST',
                url: '/issue/change',
                data: {assignment: assignment, status: status, issue:issue },
                cache: false,
                beforeSend:function(xhr){
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
                success: function(response) {
                    location.reload();
                },
                failure: function(response) {
                    alert('sorry, insert error. please try again');
                },
                complete: function(response){
                    console.log(JSON.stringify(response));
                },
            });
        }
