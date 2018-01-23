$(document).ready(function() {



    $('#test-form').bootstrapValidator({
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {


            'Row Number': {
             message: 'The name is not valid',
                validators: {

                    regexp: {
                        regexp: /^[1-9]\d*$/,
                        message: 'The row number can only accept alphabetical input'
                    },
                }
            },
            'Name': {
             message: 'The name is not valid',
                validators: {
                    notEmpty: {
                        message: 'Your name is required and cannot be empty'
                    },
                    stringLength: {
                        min: 1,
                        max: 30,
                        message: 'The name must be more than 1 and less than 30 characters long'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z ]*$/,
                        message: 'The first name can only accept alphabetical input'
                    },
                }
            },

            email: {
                validators: {
                    notEmpty: {
                        message: 'The email address is required and cannot be empty'
                    },
                    emailAddress: {
                        message: 'The email address is not a valid'
                    }
                }
            },
          }
    })
    .on('success.form.bv', function(e) {

        e.preventDefault();

        var $form = $(e.target);

        var bv = $form.data('bootstrapValidator');

        var url = 'https://script.google.com/macros/s/AKfycbwkjpThtiOa3Enfp1axgZewyjKUL0XI2hsK9plCXM-EgpU9c9CZ/exec';

      var redirectUrl = 'success-page.html';


        $('#postForm').prepend($('<span></span>').addClass('glyphicon glyphicon-refresh glyphicon-refresh-animate'));
        var jqxhr = $.post(url, $form.serialize(), function(data) {
            console.log("Success! Data: " + data.statusText);
            $(location).attr('href',redirectUrl);

        })
            .fail(function(data) {
                console.warn("Error! Data: " + data.statusText);
                // HACK

                if (navigator.userAgent.search("Safari") >= 0 && navigator.userAgent.search("Chrome") < 0) {
                    //alert("Browser is Safari -- we get an error, but the form still submits -- continue.");
                    $(location).attr('href',redirectUrl);
                }
            });
    });
});
