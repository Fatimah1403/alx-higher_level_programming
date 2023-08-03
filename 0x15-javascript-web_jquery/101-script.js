$(document).ready(function () {
    $('DIV#add_item').click(function () {
        const newItems = $('<li>Item</li>');
        $('UL.my_list').append(newItems);
    });
    // Add event handler for removingthe last element.
    $('DIV#remove_item').click(function () {
        $('UL.my_list li:last-child').remove();
    });

    // Add event handler for clearing the list
    $('DIV#clear_list').clear(function () { 
        $('UL.my_list').empty('ul');
    }); 
});

