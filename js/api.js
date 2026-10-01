// Configuração da API
const API_URL = 'https://ca-sports-backend-production.up.railway.app/api';

// Funções Utilitárias
function showToast(message, type = 'success') {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;

    container.appendChild(toast);

    setTimeout(() => {
        toast.remove();
    }, 3000);
}


// ======================================================
// PERSISTÊNCIA DO CARRINHO
// ======================================================

let cart = JSON.parse(localStorage.getItem('cart')) || [];

function saveCart() {
    localStorage.setItem('cart', JSON.stringify(cart));
}


// ======================================================
// FETCH COM AUTENTICAÇÃO
// ======================================================

async function apiFetch(endpoint, options = {}) {

    const token = localStorage.getItem('token');

    if (token) {
        options.headers = {
            ...options.headers,
            'Authorization': `Bearer ${token}`
        };
    }

    try {

        const response = await fetch(`${API_URL}${endpoint}`, options);

        const data = await response.json().catch(() => null);

        if (!response.ok) {
            throw new Error(data?.error || 'Erro na requisição');
        }

        return data;

    } catch (error) {

        if (error.message === 'Failed to fetch') {
            throw new Error('Servidor offline ou indisponível.');
        }

        throw error;
    }
}


// ======================================================
// AUTENTICAÇÃO
// ======================================================

const authModal = document.getElementById('auth-modal');
const loginForm = document.getElementById('login-form');
const registerForm = document.getElementById('register-form');
const authTabs = document.querySelectorAll('.auth-tab');


// Alternar Login / Cadastro
authTabs.forEach(tab => {

    tab.addEventListener('click', () => {

        authTabs.forEach(t => t.classList.remove('active'));

        tab.classList.add('active');

        document
            .querySelectorAll('.auth-form')
            .forEach(f => f.classList.remove('active'));

        document
            .getElementById(tab.getAttribute('data-target'))
            .classList.add('active');
    });

});


// Fechar modais
document.querySelectorAll('.modal-close').forEach(btn => {

    btn.addEventListener('click', (e) => {

        const modal = e.target.closest('dialog');

        if (modal) {
            modal.close();
        }

    });

});


// ======================================================
// LOGIN
// ======================================================

if (loginForm) {

    loginForm.addEventListener('submit', async (e) => {

        e.preventDefault();

        const email = document.getElementById('login-email').value;
        const password = document.getElementById('login-password').value;

        try {

            const data = await apiFetch('/auth/login', {

                method: 'POST',

                headers: {
                    'Content-Type': 'application/json'
                },

                body: JSON.stringify({
                    email,
                    password
                })

            });

            localStorage.setItem('token', data.token);

            localStorage.setItem(
                'user',
                JSON.stringify(data.user)
            );

            authModal.close();

            showToast('Login realizado com sucesso!');

            updateHeaderIcons();

        } catch (error) {

            showToast(error.message, 'error');

        }

    });

}


// ======================================================
// CADASTRO
// ======================================================

if (registerForm) {

    registerForm.addEventListener('submit', async (e) => {

        e.preventDefault();

        const name = document.getElementById('reg-name').value;
        const email = document.getElementById('reg-email').value;
        const password = document.getElementById('reg-password').value;

        try {

            const data = await apiFetch('/auth/register', {

                method: 'POST',

                headers: {
                    'Content-Type': 'application/json'
                },

                body: JSON.stringify({
                    name,
                    email,
                    password
                })

            });

            localStorage.setItem('token', data.token);

            localStorage.setItem(
                'user',
                JSON.stringify(data.user)
            );

            authModal.close();

            showToast('Conta criada com sucesso!');

            updateHeaderIcons();

        } catch (error) {

            showToast(error.message, 'error');

        }

    });

}


// ======================================================
// TENHO INTERESSE -> TAMANHO -> CARRINHO
// ======================================================

const sizeModal = document.getElementById('size-modal');

let selectedProductForCart = null;

let currentSize = null;


// IMPORTANTE:
// O botão "Tenho interesse" NÃO abre o WhatsApp.
// Ele apenas inicia o processo de adicionar ao carrinho.

document.addEventListener('click', (e) => {

    const btn = e.target.closest('.product-btn');

    if (!btn) return;

    // Impede qualquer link padrão
    e.preventDefault();

    // Impede que outros eventos acima sejam executados
    e.stopPropagation();

    const card = btn.closest('.product-card');

    if (!card) return;


    // ==================================================
    // VERIFICA LOGIN
    // ==================================================

    const isLogged = !!localStorage.getItem('token');

    if (!isLogged) {

        authModal.showModal();

        return;
    }


    // ==================================================
    // PEGA OS DADOS DO PRODUTO
    // ==================================================

    selectedProductForCart = {

        id:
            card.getAttribute('data-product') ||
            card.querySelector('.product-name').innerText,

        name:
            card.querySelector('.product-name').innerText,

        price:
            parseFloat(
                card.getAttribute('data-price') || 0
            ),

        image:
            card.querySelector('img').src,

        sizes:
            (card.getAttribute('data-sizes') || '').split(',')

    };


    // ==================================================
    // PREENCHE MODAL DE TAMANHO
    // ==================================================

    document.getElementById(
        'size-modal-product-name'
    ).innerText = selectedProductForCart.name;


    document.getElementById(
        'size-modal-product-price'
    ).innerText =
        'R$ ' +
        selectedProductForCart.price
            .toFixed(2)
            .replace('.', ',');


    const sizeContainer =
        document.getElementById('size-options');


    sizeContainer.innerHTML = '';

    currentSize = null;


    // ==================================================
    // CRIA BOTÕES DE TAMANHO
    // ==================================================

    selectedProductForCart.sizes.forEach(size => {

        if (!size) return;

        const sizeBtn = document.createElement('button');

        sizeBtn.className = 'size-btn';

        sizeBtn.innerText = size.trim();


        sizeBtn.addEventListener('click', () => {

            document
                .querySelectorAll('.size-btn')
                .forEach(b => b.classList.remove('active'));

            sizeBtn.classList.add('active');

            currentSize = size.trim();

        });


        sizeContainer.appendChild(sizeBtn);

    });


    // Quantidade inicial
    document.getElementById('qty-input').value = 1;


    // Abre modal de tamanho
    sizeModal.showModal();

});


// ======================================================
// QUANTIDADE
// ======================================================

document.getElementById('qty-minus')?.addEventListener('click', () => {

    const input = document.getElementById('qty-input');

    if (input.value > 1) {
        input.value = parseInt(input.value) - 1;
    }

});


document.getElementById('qty-plus')?.addEventListener('click', () => {

    const input = document.getElementById('qty-input');

    if (input.value < 99) {
        input.value = parseInt(input.value) + 1;
    }

});


// ======================================================
// ADICIONAR AO CARRINHO
// ======================================================

document
    .getElementById('add-to-cart-btn')
    ?.addEventListener('click', () => {

        // Verifica tamanho
        if (!currentSize) {

            showToast(
                'Selecione um tamanho antes de adicionar ao carrinho.',
                'error'
            );

            return;
        }


        const qty =
            parseInt(
                document.getElementById('qty-input').value
            );


        // Adiciona produto
        cart.push({

            productId:
                selectedProductForCart.id,

            name:
                selectedProductForCart.name,

            price:
                selectedProductForCart.price,

            size:
                currentSize,

            quantity:
                qty,

            subtotal:
                selectedProductForCart.price * qty,

            image:
                selectedProductForCart.image

        });


        // Salva carrinho
        saveCart();

        // Atualiza número do carrinho
        updateCartBadge();

        // Fecha modal
        sizeModal.close();


        showToast(
            `${selectedProductForCart.name} adicionado ao carrinho!`
        );

    });


// ======================================================
// CARRINHO
// ======================================================

const cartModal =
    document.getElementById('cart-modal');


document
    .getElementById('cart-btn')
    ?.addEventListener('click', () => {

        renderCart();

        cartModal.showModal();

    });


// ======================================================
// RENDERIZAR CARRINHO
// ======================================================

function renderCart() {

    const container =
        document.getElementById('cart-items');

    container.innerHTML = '';

    let total = 0;


    // Carrinho vazio
    if (cart.length === 0) {

        container.innerHTML =
            '<p>Seu carrinho está vazio.</p>';

    }

    else {

        cart.forEach((item, index) => {

            total += item.subtotal;


            const div =
                document.createElement('div');


            div.className = 'cart-item';


            div.innerHTML = `

                <img
                    src="${item.image}"
                    alt="${item.name}"
                >

                <div class="cart-item-details">

                    <h4>${item.name}</h4>

                    <p>
                        Tam: ${item.size}
                        |
                        Qtd: ${item.quantity}
                    </p>

                    <p>
                        <strong>
                            R$ ${item.subtotal
                    .toFixed(2)
                    .replace('.', ',')}
                        </strong>
                    </p>

                </div>

                <button
                    class="cart-item-remove"
                    onclick="removeFromCart(${index})"
                >
                    &times;
                </button>

            `;


            container.appendChild(div);

        });

    }


    // Atualiza total
    document.getElementById(
        'cart-total-value'
    ).innerText =
        'R$ ' +
        total.toFixed(2).replace('.', ',');

}


// ======================================================
// REMOVER PRODUTO DO CARRINHO
// ======================================================

window.removeFromCart = function (index) {

    cart.splice(index, 1);

    saveCart();

    renderCart();

    updateCartBadge();

};


// ======================================================
// BADGE DO CARRINHO
// ======================================================

function updateCartBadge() {

    const badge =
        document.getElementById('cart-badge');


    if (!badge) return;


    if (cart.length > 0) {

        badge.style.display = 'block';

        badge.innerText = cart.length;

    }

    else {

        badge.style.display = 'none';

    }

}


// ======================================================
// CHECKOUT
// ======================================================

document
    .getElementById('checkout-btn')
    ?.addEventListener('click', async () => {


        // ==============================================
        // VERIFICA SE EXISTEM PRODUTOS
        // ==============================================

        if (cart.length === 0) {

            showToast(
                'Adicione produtos ao carrinho antes de enviar.',
                'error'
            );

            return;
        }


        // ==============================================
        // CALCULA TOTAL
        // ==============================================

        const total =
            cart.reduce(
                (acc, item) =>
                    acc + item.subtotal,
                0
            );


        // ==============================================
        // MONTA MENSAGEM DO WHATSAPP
        // ==============================================

        let mensagem =
            `Olá! Gostaria de fazer este pedido:\n\n`;


        cart.forEach((item) => {

            mensagem +=
                `🛍️ ${item.name}\n`;

            mensagem +=
                `📏 Tamanho: ${item.size}\n`;

            mensagem +=
                `🔢 Quantidade: ${item.quantity}\n`;

            mensagem +=
                `💵 Preço: R$ ${item.price
                    .toFixed(2)
                    .replace('.', ',')}\n`;

            mensagem +=
                `💰 Subtotal: R$ ${item.subtotal
                    .toFixed(2)
                    .replace('.', ',')}\n\n`;

        });


        mensagem +=
            `🧾 TOTAL DO PEDIDO: R$ ${total
                .toFixed(2)
                .replace('.', ',')}\n\n`;

        mensagem +=
            `Gostaria de confirmar meu pedido!`;


        // ==============================================
        // WHATSAPP DA LOJA
        // ==============================================

        const numeroWhatsApp =
            '5579981246335';


        const urlWhatsApp =
            `https://wa.me/${numeroWhatsApp}?text=${encodeURIComponent(mensagem)}`;


        // ==============================================
        // DADOS DO PEDIDO
        // ==============================================

        const orderData = {

            items: cart,

            total: total

        };


        try {

            // ==========================================
            // SALVA PEDIDO NO BANCO
            // ==========================================

            await apiFetch('/orders', {

                method: 'POST',

                headers: {
                    'Content-Type': 'application/json'
                },

                body:
                    JSON.stringify(orderData)

            });


            // ==========================================
            // LIMPA O CARRINHO
            // ==========================================

            cart = [];

            saveCart();

            updateCartBadge();


            // ==========================================
            // FECHA CARRINHO
            // ==========================================

            cartModal.close();


            // ==========================================
            // ABRE WHATSAPP
            // ==========================================

            window.location.href =
                urlWhatsApp;


        }

        catch (error) {

            showToast(
                error.message,
                'error'
            );

        }

    });


// ======================================================
// ÁREA DO USUÁRIO
// ======================================================

const userModal =
    document.getElementById('user-modal');


document
    .getElementById('user-btn')
    ?.addEventListener('click', async () => {


        // Verifica login
        const isLogged =
            !!localStorage.getItem('token');


        if (!isLogged) {

            authModal.showModal();

            return;

        }


        // ==============================================
        // INFORMAÇÕES DO USUÁRIO
        // ==============================================

        const user =
            JSON.parse(
                localStorage.getItem('user')
            );


        if (user) {

            document.getElementById(
                'user-info-name'
            ).innerText =
                user.name;


            document.getElementById(
                'user-info-email'
            ).innerText =
                user.email;

        }


        // ==============================================
        // BUSCA PEDIDOS
        // ==============================================

        const ordersContainer =
            document.getElementById(
                'user-orders'
            );


        ordersContainer.innerHTML =
            '<p>Carregando pedidos...</p>';


        try {

            const data =
                await apiFetch('/orders');


            if (data.orders.length === 0) {

                ordersContainer.innerHTML =
                    '<p>Você ainda não tem pedidos.</p>';

            }

            else {

                ordersContainer.innerHTML =
                    data.orders.map(o => `

        <div
            style="
                background: #222;
                padding: 10px;
                margin-bottom: 10px;
                border-radius: 6px;
            "
        >

            <p>
                <strong>
                    Pedido #${o.id.substring(18)}
                </strong>
            </p>

            <p>
                Total:
                R$ ${o.total
                            .toFixed(2)
                            .replace('.', ',')}
            </p>

        </div>

    `).join('');

            }

        }

        catch (error) {

            ordersContainer.innerHTML =
                '<p style="color:#e74c3c;">Erro ao carregar pedidos.</p>';

        }


        userModal.showModal();

    });


// ======================================================
// LOGOUT
// ======================================================

document
    .getElementById('logout-btn')
    ?.addEventListener('click', () => {

        localStorage.removeItem('token');

        localStorage.removeItem('user');

        cart = [];
        saveCart();

        userModal.close();

        showToast('Você saiu da conta.');

        updateHeaderIcons();

    });


// ======================================================
// ATUALIZA ÍCONES
// ======================================================

function updateHeaderIcons() {

    updateCartBadge();

}


// ======================================================
// INICIALIZAÇÃO
// ======================================================

updateHeaderIcons();