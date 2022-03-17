console.log("TEST");

let stripe = Stripe('pk_test_51KPpqoJAp5w3wtxOcLHWfFgiHHtZGpp0tNj4ecSzSQSWJiCZoKIZxcLN06mdCEFAMRyTuIu9qVDaXH0NMxF1Yur1009lNv4heh');
let elements = stripe.elements();
let card = elements.create('card', { style: style });
card.mount('#card-element');