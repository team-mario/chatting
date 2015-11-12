$(function () {
    $('#btn_create_issue').click(function(){
        $('#create-issue-modal').modal('toggle');
    });
    $('#btn_create_team').click(function(){
        $('#create-team-modal').modal('toggle');
    });
    $('#btn_setting').click(function(){
        $('#create-setting-modal').modal('toggle');
    });
});
$(function (){
    $('#item_upload_file').click(function(){
        $('#FileUploadModal').modal('toggle');
    });
});

$(function (){
    $('#item_add_hash_tag').click(function(){
        $('#HashTagAddModal').modal('toggle');
    });
});