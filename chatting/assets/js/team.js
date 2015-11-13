$(function(){
    $("#team_select_dialog").dialog({
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
    $("#btn_select_team").on("click",function(){
        $("#team_select_dialog").dialog("open");
    });

    $('#team_select_dialog').on('dialogclose', function(event) {
        var ul = document.getElementById("list");
        while(ul.firstChild ){
            ul.removeChild(ul.firstChild);
        }
    });
});
function add_team(team_name){
    var ul = document.getElementById("team_list");
    var li = document.createElement("li");
    li.setAttribute("id", "element");
    var a = document.createElement('a');
    var linkText = document.createTextNode(team_name);
    a.appendChild(linkText);
    a.title = team_name;
    var temp_href = "/team/detail/";
    a.href = temp_href+team_name;
    li.appendChild(document.body.appendChild(a));
    ul.appendChild(li);
}
