document.addEventListener('DOMContentLoaded', () => {

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
       }


    var updateLinks = document.querySelectorAll('.update-link');
    updateLinks.forEach(link => {
        link.addEventListener('click', () => {
            var itemName = link.parentElement.parentElement.parentElement.parentElement.children[0].innerHTML;
            var itemId = link.parentElement.parentElement.parentElement.parentElement.children[1].innerHTML;
            var itemAmount = link.parentElement.parentElement.parentElement.parentElement.children[2].innerHTML;
            var itemStatus = link.parentElement.parentElement.parentElement.parentElement.children[3].innerHTML;
            // console.log(itemId, itemName, itemAmount, itemStatus);

            const tobeUpdatedItemId = JSON.stringify({'id': itemId});
            const request = new XMLHttpRequest();
            const csrftoken = getCookie('csrftoken');
            request.open('POST', `/edit/${itemId}`);
            request.setRequestHeader("Content-Type", "application/json");
            if (csrftoken){
              request.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
              request.setRequestHeader("X-Requested-With", "XMLHttpRequest")
              request.setRequestHeader("X-CSRFToken", csrftoken)
            }
            request.onload = () => {
                // console.log(request.response);
            };
            request.send(tobeUpdatedItemId);
        });
    });
});