$().ready(function () {
    console.log("function called");

    $("#registrainForm").validate({

        rules: {
            name: {
                required: true,
                minlength: 3
            },
            email: {
                required: true,
                email: true
            },
            password: {
                required: true,
                minlength: 5
            },
            confirmPassword: {
                required: true,
                equalTo: "#password"
            }
        },
        messages: {
            name: {
                required: "Enter Name",
                minlength: "Name must be 3 char long"
            },
            email: "Enter valid email",
            password: {
                required: "Password require.",
                minlength: "Minimum 5 digit required"
            },
            confirmPassword: {
                required: "Enter Password Again",
                equalTo: "Password not match"
            }
        },

        errorElement: "span",
        errorPlacement: function (error, element) {
            error.css({ "color": "red", "font-size": "10px" });

            if (element.prop("type") == "checkbox") {
                error.insertAfter(element.parent("div"));
            } else {
                error.insertAfter(element);
            }
        },
        highlight: function (element) {
            $(element).css({ "border": "1px solid red" })
        },
        unhighlight: function (element) {
            $(element).css({ "border": "1px solid green" })
        },

        submitHandler: function (form) {
            /*   swal({
                  title: "Good Job!",
                  text: "Click Ok to register.",
                  icon: "success"
              }); */
            form.submit();
        }
    });
});

