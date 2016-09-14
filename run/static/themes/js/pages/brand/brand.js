$(document).ready(function () {
    $('#myTable').DataTable();

    var div_page_wrapper = $('#page-wrapper');
    var add_brand = $('#add_brand');
    var modal_brand = $('#modal_brand');
    var form_brand;

    div_page_wrapper.on('click', "#add_brand", function(e) {
        e.preventDefault();
        add_brand.attr("disabled",true);
        $.ajax({
            type: "GET",
            url: URL_BRAND_ADD
        }).done(function(data) {
             modal_brand.html(data);
             modal_brand.modal({backdrop: 'static', keyboard: false});
        }).always(function() {
              add_brand.attr("disabled",false);
        });
    });


    div_page_wrapper.on('click', '#save_brand', function(e) {
        form_brand = $('#form_person');
        var parameter = {
            'form': get_FormDataserialize(form_brand)
        };
        $.ajax({
            type: "POST",
            url: URL_BRAND_ADD,
            data: JSON.stringify(parameter)
        }).done(function(data) {
             modal_brand.modal('hide');
             swal("Successfull!", "Add new Brand", "success")
        })
    });


    div_page_wrapper.on('click', '.brand_edit', function (e) {
        e.preventDefault();
        var person_id = $(this).attr('data-id');
        var parameter = {
            'person_id': person_id
        };
        $.ajax({
            type: "GET",
            url: URL_BRAND_EDIT,
            data: parameter
        }).done(function(data) {
           modal_brand.html(data);
           modal_brand.modal({backdrop: 'static', keyboard: false});
        })
    });


    div_page_wrapper.on('click', '#update_brand', function (e) {
        e.preventDefault();
        var form_pk = $(this).attr('data-id');
        form_brand = $('#form_brand');
        var parameter = {
            'form': get_FormDataserialize(form_brand),
            'form_pk': form_pk
        };
        $.ajax({
            type: "POST",
            url: URL_BRAND_EDIT,
            data: JSON.stringify(parameter)
        }).done(function(data) {
           modal_brand.modal('hide');
           swal("Successfull!", "", "success")
        }).always(function() {
            $.get(URL_BRAND_LIST, function(data){
                $("#list_table").html(data);
    	    });
        });

    });

})