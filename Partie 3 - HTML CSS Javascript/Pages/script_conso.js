document.getElementById('submit-button').addEventListener('click', () => {
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;

    // Vérification des dates
    if (!startDate || !endDate || endDate < startDate) {
        alert("Veuillez sélectionner une plage de dates valide.");
        return;
    }

    // Mise à jour de l'URL de l'iframe avec les paramètres
    const iframe = document.getElementById('graph-frame');
    iframe.src = `http://127.0.0.1:8000/factures/conso_chart/?start_date=${startDate}&end_date=${endDate}`;
});