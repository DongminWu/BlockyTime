function input_area_event_handler(input, name_text) {

    new_content = input.value
    name_text.text(new_content)
    input.remove();
    name_text.show();
}

function turn_to_editable(e) {
    name_obj = e.parent().siblings(".categories_name")
    name_text = name_obj.children(".name_text")
    var ori_content = name_obj.text().trim()
    console.log(name_obj.text())
    name_text.hide();
    // Create an input
    input = document.createElement("input");
    input.type = "text";
    input.size = ori_content.length;
    input.value = ori_content
    input.style.fontSize = "1.2em"
    input.setSelectionRange(0, input.value.length)

    e.parents(".categories_extended").hide()
    name_obj.append(input)

    // Focus it, hook blur to undo
    input.focus();
    input.onblur = function () {
        input_area_event_handler(input, name_text)
    }
    input.onkeypress = function (e) {
        if (e.keyCode == 13) {
            input_area_event_handler(input, name_text)

        }
    }


}

function secondary_add_handler(e) {
    new_secondary = $("#secondary_template #secondary").clone(true)
    new_secondary.insertAfter(e)
    new_edit = new_secondary.find(".categories_edit")
    turn_to_editable(new_edit)
}

$(document).ready(function () {


    //categories tab
    $(".categories_extended").hide()
    $(".categories_name").click(function () {
        $(this).siblings(".categories_extended").toggle("fast");
        $(this).parent().siblings().children(".categories_extended").hide()
    })

    //edit
    $(".categories_edit").click(
        function () {

            turn_to_editable($(this))

        })

    //delete
    var current_category;
    var current_categories_group;
    $(".categories_delete").click(function () {
        current_category = $(this).parents(".categories")
        current_categories_group = $(this).parents(".categories_group")
    })
    $(".delete_warning_modal #yes_button").click(
        function () {
            if (current_category.attr('id') == 'secondary') {
                console.log("delete myself")
                current_category.remove()
            } else if (current_category.attr('id') == 'primary') {
                console.log("delete the group")
                current_categories_group.remove()
            }
        }
    )

    //add
    $("#secondary_add").click(function () {
        secondary_add_handler($(this))
    })
    $("#primary_add").click(function () {
        new_primary_group = $("#primary_template").clone(true)
        new_primary_group.addClass("categories_group")
        new_primary_group.insertAfter($(this))
        new_edit = new_primary_group.find("#primary").find(".categories_edit")
//        new_primary_group.find("#secondary_add").click(function () {
//        new_primary_group.find("#secondary_add").click(function () {
//            secondary_add_handler($(this)) //rebinding handler
//        })
        turn_to_editable(new_edit)
    })


});
