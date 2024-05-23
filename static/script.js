$(document).ready(function() {
    const currencyDataElement = $('#currency-data');
    const currencyList = JSON.parse(currencyDataElement.attr('data-currencies'));

    const baseCurrencySelect = $('#base_currency');
    const targetCurrencySelect = $('#target_currency');

    // Populate dropdowns with currencies
    currencyList.forEach(currency => {
        baseCurrencySelect.append(new Option(currency, currency));
        targetCurrencySelect.append(new Option(currency, currency));
    });

    $('#convert-form').on('submit', function(event) {
        event.preventDefault();
        $.ajax({
            url: '/convert',
            method: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                if (response.success) {
                    $('#result').text('Converted Amount: ' + response.converted_amount);
                } else {
                    $('#result').text('Error: ' + response.error);
                }
            }
        });
    });

    $('#swap-button').on('click', function() {
        const baseCurrency = baseCurrencySelect.val();
        const targetCurrency = targetCurrencySelect.val();
        
        baseCurrencySelect.val(targetCurrency);
        targetCurrencySelect.val(baseCurrency);
    });
});
