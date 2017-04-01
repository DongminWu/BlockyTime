function input_area_event_handler(input,name_text) {

    new_content = input.value
    name_text.text(new_content)
    input.remove();
    name_text.show();
}

$(document).ready(function () {


    //categories tab
    $(".categories_extended").hide()
    $(".categories_name").click(function () {
        $(this).siblings(".categories_extended").toggle("fast");
        $(this).parent().siblings().children(".categories_extended").hide()
    })
    $(".categories_edit").click(
        function () {
            name_obj = $(this).parent().siblings(".categories_name")
            name_text = name_obj.children(".name_text")
            var ori_content = name_obj.text().trim()
            name_text.hide();
            // Create an input
            input = document.createElement("input");
            input.type = "text";
            input.size = ori_content.length;
            input.value = ori_content
            input.style.fontSize = "1.2em"
            input.setSelectionRange(0, input.value.length)
            name_obj.append(input)

            // Focus it, hook blur to undo
            input.focus();
            input.onblur = function(){
                input_area_event_handler(input,name_text)
            }
            input.onkeypress = function(e)
            {
                if(e.keyCode == 13){
                input_area_event_handler(input,name_text)
                    
                }
            }



        })

});
