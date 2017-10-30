'use strict'

$(function() {

    $('.blog-content').hide()
    $('#edit').hide()
    $('#submit').hide()
    $('form').hide()

    $('.blog-post').on('click', function(){
        console.log(this)
        $('.blog-content').show()
        $('.blog-post').hide();
        $(this).fadeIn()
        $('#new-entry').hide()
        $('#edit').fadeIn()
    })

    function showNewEntry(){
        $('#new-entry-button').on('click', function(){
            $('.blog').hide();
            $('form').fadeIn();
            $('#new-entry-button').hide();
            $('#submit').fadeIn();

        })
    }

    $('#submit').on('click', function(){
        console.log('new entry?')
        var handlebarsData = {
            title: $('form input').val(),
            content: $('#content').val(),
            date: new Date()
        }
        console.log(handlebarsData)
        var template = $('#template').html();
        var compileData = Handlebars.compile(template)
        $('.blog').append(compileData(handlebarsData))
    })

    $('#home').on('click', function(){
            $('.blog').fadeIn();
            $('form').hide();
            $('.blog-content').hide()
            $('#new-entry-button').fadeIn();
            $('#submit').hide();
    })


    showNewEntry()
})