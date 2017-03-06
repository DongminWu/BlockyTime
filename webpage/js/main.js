function EnsureVertical(e) {
    if ($(".timetable").css("max-height") != "100%") {
        console.log("Vertical mode")
        e();
    }


}

function SwitchTimetableAndCategory() {
    $(".timetable").slideToggle("fast", function () {
        $("#catagory_and_date").toggleClass("catagory_and_date")
        $("#catagory_and_date").toggleClass("catagory_and_date_expand")

    });

    //    $(".catagory").slideTooggle("fast");

}

function SelectActivedTimetableItem(e) {
    //    console.log($(".timetable_plane").find("label").text());
    $(".timetable_plane").find(".active").each(
        function () {
            e($(this));
        });


}

$(document).ready(function () {
    $(".primary_category").siblings("ul").hide();

    EnsureVertical(function () {
        console.log("hello");

    })


    $(".primary_category").click(function () {
        $(".primary_category").siblings("ul").slideToggle("fast");
    })

    $(".second_category").click(function () {
        SelectActivedTimetableItem(function (e) {
            e.removeClass("active");
        });
        $(this).parent().parent("ul").slideUp("fast");


        //        console.log($(this).parent("ul"));
    })


    //vertical mode

    $(".catagory_title").click(function () {
        EnsureVertical(function () {
            SwitchTimetableAndCategory();
        })
    })

    $(".second_category").click(function () {
        EnsureVertical(function () {
            SwitchTimetableAndCategory();
        })
    });

})
