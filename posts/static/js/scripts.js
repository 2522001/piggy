/*!
* Start Bootstrap - Shop Homepage v5.0.5 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

function search_enter(e) {
    if (e.keyCode == 13) {
        $("#kw").val($(".kw").val());
        // $("#page").val(1);
        $("#searchForm").submit();
    }
}

// const page_elements = document.getElementsByClassName("page-link");
// Array.from(page_elements).forEach(function(element) {
//     element.addEventListener('click', function() {
//         // document.getElementById('page').value = this.dataset.page;
//         document.getElementById('searchForm').submit();
//     });
// });

const btn_search = document.getElementById("btn_search");
btn_search.addEventListener('click', function() {
    document.getElementById('kw').value = document.getElementById('search_kw').value;
    // document.getElementById('page').value = 1;  // 검색버튼을 클릭할 경우 1페이지부터 조회한다.
    document.getElementById('searchForm').submit();
});