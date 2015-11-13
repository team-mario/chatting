$(function () {
    $("#dialog").dialog({
        autoOpen:false,
        position:[100,200],
        modal:true,
        resizable:false,
        buttons:{
            "확인":function(){
                $(this).dialog("close");
            },"취소":function(){
                $(this).dialog("close");
            }
        }
    });

    //simple click events
    $("#btn_information").on("click",function(){
        $("#dialog").dialog("open");
    });

    $("#btn_invite").on("click",function(){
        $('#create-invite-modal').modal('toggle');
    });

    $('#btn_create_issue').click(function(){
        $('#create-issue-modal').modal('toggle');
    });

    $('#btn_create_team').click(function(){
        $('#create-team-modal').modal('toggle');
    });

    $('#btn_setting').click(function(){
        $('#create-setting-modal').modal('toggle');
    });

    $('#item_upload_file').click(function(){
        $('#FileUploadModal').modal('toggle');
    });

    $('#item_add_hash_tag').click(function(){
        $('#HashTagAddModal').modal('toggle');
    });
});
