document.getElementById('add_item').addEventListener('click', function () {
    const newItem = docuemnt.createElement('li');
    newItem.textContent = 'Item';
    document.querySelector('.my_lsit').appendChild(newItem);
});