const express = require('express');
const mercadopago = require('mercadopago');

const app = express();

mercadopago.configure({
    access_token: 'APP_USR-7088407773309513-092312-59bbf54bf6a0f1aa0de3f73f6150ab60-444959623'
});

// Rota para gerar o link de pagamento
app.get('/gerar-link-pagamento', async (req, res) => {
    let preference = {
        items: [
            {
                id: 'ribs-brisket-and-burnt-ends',
                title: "Joe's KC BBQ",
                unit_price: 110.99,
                quantity: 1,
                currency_id: 'BRL',
            },
            {
                id: "005-kings-carolina-oink-sampler",
                title: "Kings BBQ",
                unit_price: 89,
                quantity: 1,
                currency_id: "BRL",
            },
            {
                id: "texas-monthlys-1-bbq-brisket",
                title: "Snow's BBQ",
                unit_price: 199,
                quantity: 1,
                currency_id: "BRL",
            },
            {
                id: "whole-brisket-texas-bbq-sauce",
                title: "Franklin Barbecue",
                unit_price: 249,
                quantity: 1,
                currency_id: "BRL",
            },
            {
                id: "whole-texas-smoked-brisket",
                title: "Terry Black's Barbecue",
                unit_price: 189,
                quantity: 1,
                currency_id: "BRL",
            },
            {
                id: "mini-trinity-bbq-combo-brisket-ribs-and-links",
                title: "Bludso's BBQ",
                unit_price: 139,
                quantity: 1,
                currency_id: "BRL",
            },
            {
                id: "235203-blue-smoke-baby-back-ribs-backyard-barbecue-chicken-combo",
                title: "Blue Smoke",
                unit_price: 129,
                quantity: 1,
                currency_id: "BRL",
            },
            {
                id: "006-kings-meat-lovers-special",
                title: "Kings BBQ",
                unit_price: 139,
                quantity: 1,
                currency_id: "BRL",
            },
            {
                id: "the-big-ugly-bbq-dinner-for-6",
                title: "Ugly Drum",
                unit_price: 229,
                quantity: 1,
                currency_id: "BRL",
            },
            {
                id: "17796-mighty-quinns-bbq-sampler-pack",
                title: "Mighty Quinn's BBQ",
                unit_price: 169,
                quantity: 1,
                currency_id: "BRL",
            },
            {
                id: "post-oak-smoked-half-brisket",
                title: "Southside Market & Barbeque",
                unit_price: 109,
                quantity: 1,
                currency_id: "BRL",
            },
            {
                id: "best-of-texas-bbq-combo-serves-14",
                title: "Snow's BBQ",
                unit_price: 269,
                quantity: 1,
                currency_id: "BRL",
            },
            {
                id: 'the-gramercy-tavern-burger-4-pack',
                title: "Gramercy Tavern",
                unit_price: 99,
                quantity: 1,
                currency_id: 'BRL',
            },
            {
                id: 'shake-shack-shackburger-8-pack',
                title: "Shake Shack",
                unit_price: 49,
                quantity: 1,
                currency_id: 'BRL',
            },
            {
                id: 'gotts-cheeseburger-kit-for-4',
                title: "Gott's Roadside",
                unit_price: 99,
                quantity: 1,
                currency_id: 'BRL',
            },
            {
                id: 'le-big-matt-kit-for-6',
                title: "Emmy Squared",
                unit_price: 99,
                quantity: 1,
                currency_id: 'BRL',
            },
            {
                id: 'shake-shack-shackburger-16-pack',
                title: "Shake Shack",
                unit_price: 89,
                quantity: 1,
                currency_id: 'BRL',
            },
            {
                id: '21-usda-prime-burgers-pack-of-18-8oz-each',
                title: "Peter Luger Steak House",
                unit_price: 175.95,
                quantity: 1,
                currency_id: 'BRL',
            },
            {
                id: 'double-stack-burger-kit-for-4',
                title: "Holeman & Finch",
                unit_price: 79,
                quantity: 1,
                currency_id: 'BRL',
            },
            {
                id: 'goldbelly-burger-bash-pack',
                title: "Pat LaFrieda Meats",
                unit_price: 109,
                quantity: 1,
                currency_id: 'BRL',
            },
            {
                id: 'burger-au-poivre-kit-4-pack',
                title: "Raoul's",
                unit_price: 99,
                quantity: 1,
                currency_id: 'BRL',
            },
            {
                id: 'goldbelly-burger-blend-4-lbs',
                title: "Flannery Beef",
                unit_price: 79,
                quantity: 1,
                currency_id: 'BRL',
            },
            {
                id: 'gotts-complete-cheeseburger-kit-for-8',
                title: "Gott's Roadside",
                unit_price: 149,
                quantity: 1,
                currency_id: 'BRL',
            },
            {
                id: 'gramercy-tavern-burger-kielbasa-combo',
                title: "Gramercy Tavern",
                unit_price: 149,
                quantity: 1,
                currency_id: 'BRL',
            },
            {
                id: "15259-german-chocolate-killer-brownie-tin-pack",
                title: "Killer Brownie®",
                unit_price: 39.99,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "jacques-world-famous-chocolate-chip-cookies",
                title: "Jacques Torres Chocolate",
                unit_price: 39.95,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "luigis-original-cannoli-pie",
                title: "The Cannoli Pie Company",
                unit_price: 69,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "sea-salted-caramel-swirl-cheesecake",
                title: "Cotton Blues Cheesecake Company",
                unit_price: 65,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "brooklyn-blackout-cookie-brownie-combo-pack-2-tins",
                title: "Brooklyn Blackout Company",
                unit_price: 89,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "best-seller-cupcake-dozen",
                title: "Crave Cupcakes",
                unit_price: 89,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "choose-your-own-ice-cream-donuts-6-pack",
                title: "Elegant Desserts",
                unit_price: 69,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "17481-jewish-dessert-3-pack",
                title: "Ess-a-Bagel",
                unit_price: 89.95,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "dessert-bar-care-package",
                title: "Bread and Roses Bakery",
                unit_price: 65,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "donut-cookies-12-pack",
                title: "Stan's Donuts",
                unit_price: 49,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "gulab-jamun-ice-cream-cakes-2-pack",
                title: "Malai Ice Cream",
                unit_price: 79,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "jacques-world-famous-chocolate-chip-cookies-12-pack",
                title: "Jacques Torres Chocolate",
                unit_price: 69.95,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "hong-kong-boba-tea-kit-for-6",
                title: "New Territories",
                unit_price: 59,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "guys-caliente-margaritas-for-12",
                title: "Guy Fieri",
                unit_price: 69,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "woodford-reserve-mint-julep-syrup",
                title: "Woodford Reserve",
                unit_price: 39,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "new-orleans-hurricane-mix",
                title: "Franco's Hurricane Mix",
                unit_price: 39,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "margarita-mix",
                title: "Johnny Sanchez",
                unit_price: 59,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "woodford-reserve-mint-julep-syrup-2-pack",
                title: "Woodford Reserve",
                unit_price: 59,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "unicorn-parade-milkshake-kit-for-8",
                title: "New Territories",
                unit_price: 109,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "chickpea-chiller-kit-for-6",
                title: "The Hummus & Pita Co.",
                unit_price: 89,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "15194-old-honey-barn-mint-julep-mixer-200ml",
                title: "Old Honey Barn Mint Julep",
                unit_price: 25,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "kentucky-derby-mint-julep-gift-set",
                title: "Woodford Reserve",
                unit_price: 59.95,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "002-charleston-bloody-mary-mix-weekender-bold-and-spicy",
                title: "Charleston Beverage Company",
                unit_price: 39.95,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "nola-cold-brew-concentrate-bag-in-box",
                title: "Grady's Cold Brew",
                unit_price: 40,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "2-lou-malnatis-deep-dish-pizzas",
                title: "Lou Malnati's Pizza",
                unit_price: 67.99,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "23699-choose-your-own-thin-crust-pizza-4-pack",
                title: "Bartolini's",
                unit_price: 139,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "choose-your-own-new-haven-style-pizza-6-pack",
                title: "Zuppardi's Apizza",
                unit_price: 79,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "6-lou-malnatis-deep-dish-pizzas",
                title: "Lou Malnati's Pizza",
                unit_price: 116.99,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "wood-fired-pizzas-best-seller-4-pack",
                title: "Pizzeria Bianco",
                unit_price: 129,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "236991-choose-your-own-deep-dish-pizza-3-pack",
                title: "Bartolini's",
                unit_price: 139,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "choose-your-own-detroit-style-pizza-3-pack",
                title: "Emmy Squared",
                unit_price: 89,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "brooklyn-pizza-choose-your-own-5-pack",
                title: "Paesan's Pizza",
                unit_price: 69,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "choose-your-own-chicago-deep-dish-pizza-4-pack",
                title: "My Pi Pizza",
                unit_price: 129,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "4-lou-malnatis-deep-dish-pizzas",
                title: "Lou Malnati's Pizza",
                unit_price: 96.99,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "tonys-custom-pizza-3-pack",
                title: "Tony's Pizza Napoletana",
                unit_price: 99,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "plain-thin-crust-pizza-4-pack",
                title: "The Columbia Inn",
                unit_price: 79,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "california-reserve-filet-mignon-steaks-gift-box",
                title: "Flannery Beef",
                unit_price: 129,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "steaks-and-cakes-date-night-dinner-for-2",
                title: "Chesapeake Bay Gourmet",
                unit_price: 129,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "Prime-holiday-steak-sampler-for-10-12",
                title: "Saltbrick Prime",
                unit_price: 179,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "bone-in-rib-steak",
                title: "Old Homestead Steakhouse",
                unit_price: 159,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "american-wagyu-gold-grade-top-sirloins",
                title: "Snake River Farms",
                unit_price: 119,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "2-peter-luger-steak-pack-b",
                title: "Peter Luger Steak House",
                unit_price: 215.95,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "ribeye-prime-steak-gift-box",
                title: "Churchill's Steakhouse",
                unit_price: 229,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "dry-aged-usda-prime-black-angus-porterhouse-steak-2-pack",
                title: "Pat LaFrieda Meats",
                unit_price: 96.7,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "california-reserve-ribeye-steak",
                title: "Flannery Beef",
                unit_price: 32,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "dry-aged-boneless-ribeye-steak-dinner-kit-for-4",
                title: "Chef Francis Mallmann",
                unit_price: 225,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "california-reserve-filet-mignon-steak",
                title: "Flannery Beef",
                unit_price: 22,
                quantity: 1,
                currency_id: "BRL"
            },
            {
                id: "mesquite-smoked-peppered-beef-tenderloin",
                title: "Perini Ranch Steakhouse",
                unit_price: 165,
                quantity: 1,
                currency_id: "BRL"
            },



        ],
        back_urls: {
            success: 'http://127.0.0.1:5500/compracerta',
            failure: 'http://127.0.0.1:5500/compraerrada',
            pending: 'http://127.0.0.1:5500/compraerrada',
        },
        auto_return: 'approved',
    };

    try {
        const response = await mercadopago.preferences.create(preference);
        const linkPagamento = response.body.init_point;
        res.json({ link_pagamento: linkPagamento });
    } catch (error) {
        console.error(error);
        res.status(500).send('Erro ao criar preferência de pagamento');
    }
});

app.get('/compracerta', (req, res) => {
    res.send('Compra concluída com sucesso!');
});

app.get('/compraerrada', (req, res) => {
    res.send('A compra não foi realizada.');
});

app.listen(3000, () => {
    console.log('Servidor rodando na porta 3000');
});
