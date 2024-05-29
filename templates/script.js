
function generateTableRows() {
    var rowsCount = 10;
    var tbody = document.getElementById('myTable');

    for (var i = 0; i < rowsCount; i++) {
        var row = document.createElement('tr');
        for (var j = 0; j < 3; j++) {
            var cell = document.createElement('td');
            row.appendChild(cell);
        }
        tbody.appendChild(row);
    }
}
generateTableRows();

var ws;

function connect() {
    ws = new WebSocket("ws://localhost:8000/ws");
    ws.onmessage = function(event) {
        var dataList = JSON.parse(event.data);
        addRowToTable(dataList);
    };
}
connect();

function addRowToTable(data) {
    for (var i = 0; i < 10; i++) {
        var selector1 = `#myTable tr:nth-child(${i+1}) td:nth-child(1)`;
        var nameCell = document.querySelector(selector1);

        var selector2 = `#myTable tr:nth-child(${i+1}) td:nth-child(2)`;
        var symbolCell = document.querySelector(selector2);

        var selector3 = `#myTable tr:nth-child(${i+1}) td:nth-child(3)`;
        var priceCell = document.querySelector(selector3);

        var name = data[i].name;
        var price = data[i].price;

        //var name_click = document.querySelector(selector1)

        nameCell.textContent = name
        symbolCell.textContent = data[i].symbol;
        priceCell.textContent = data[i].price;

    }
    // Получаем ссылку на таблицу
    var table = document.getElementById('myTable');

    // Добавляем обработчик события к таблице
    table.addEventListener('click', function(event) {
        // Проверяем, был ли клик на ячейке с именем (td элементе)
        if (event.target.tagName === 'TD' && event.target.parentElement.parentNode.id === 'myTable') {
            // Получаем текст ячейки "Name" в строке, по которой был клик
            var name = event.target.textContent;

            var name_product = document.getElementById('name_product');
            var price_sell = document.getElementById('price_sell');
            var price_buy = document.getElementById('price_buy');

            name_product.textContent = name


            var price = event.target.nextElementSibling.nextElementSibling.textContent;
            price_sell.textContent = price;

            price_buy.textContent = parseInt(price, 10) + 1

            // Выполняем необходимые действия при клике на имя объекта
            console.log('Вы кликнули на имя объекта:', name);

            // Дополнительные действия можно добавить здесь
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const btn_sell = document.getElementById('btn_sell');
    const btn_buy = document.getElementById('btn_buy');
    const list_apps = document.getElementById('list_apps');

    list_apps.addEventListener('click', (event) => {
        event.preventDefault();
        window.open('http://127.0.0.1:8000/list-applications', '_blank');
    });

    btn_sell.addEventListener('click', (event) => {
        event.preventDefault();
        var side = 'sell';
        var price_sell = document.getElementById('price_sell').textContent;
        var name = document.getElementById('name_product').textContent;
        var amount = document.getElementById('summa').value;

        console.log('Side:', side);
        console.log('Name:', name);
        console.log('Price Sell:', price_sell);
        console.log('Amount:', amount);

        const statuses = ['Active', 'Filled', 'Rejected', 'Cancelled'];
        const randomStatus = statuses[Math.floor(Math.random() * statuses.length)];

        // Отправляем запрос POST на API
        const response = fetch('http://127.0.0.1:8000/applications/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                creation_time: new Date().toISOString().replace('T', ' ').replace('Z', ''),
                change_time: new Date().toISOString().replace('T', ' ').replace('Z', ''),
                status: randomStatus,
                side: side,
                price: price_sell,
                amount: amount,
                instrument: name
            })
        });

    });

    btn_buy.addEventListener('click', (event) => {
        event.preventDefault();
        var side = 'buy';
        var name = document.getElementById('name_product').textContent;
        var price_buy = document.getElementById('price_buy').textContent;
        var amount = document.getElementById('summa').value;

        console.log('Side:', side);
        console.log('Name:', name);
        console.log('Price Buy:', price_buy);
        console.log('Amount:', amount);

        // Отправляем запрос POST на API
        const response = fetch('http://127.0.0.1:8000/applications/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                creation_time: new Date().toISOString().replace('T', ' ').replace('Z', ''),
                change_time: new Date().toISOString().replace('T', ' ').replace('Z', ''),
                status: 'active',
                side: side,
                price: price_buy,
                amount: amount,
                instrument: name
            })
        });

    });
});
