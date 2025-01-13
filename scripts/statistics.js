const dataHeroStats = document.querySelector('#main-tour-statistics tbody');

function displayDataInTable(data) {
    data.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
        <td>${item.id}</td>
        <td>${item.hero}</td>
        <td>${item.t_picks}</td>
        <td>${item.t_wins}</td>
        <td>${item.t_losses}</td>
        <td>${item.t_wr}</td>
        <td>${item.percent_t}</td>
        <td>${item.t_picks_r}</td>
        <td>${item.t_wins_r}</td>
        <td>${item.t_losses_r}</td>
        <td>${item.t_wr_r}</td>
        <td>${item.t_picks_d}</td>
        <td>${item.t_wins_d}</td>
        <td>${item.t_losses_d}</td>
        <td>${item.t_wr_d}</td>
        <td>${item.t_bans}</td>
        <td>${item.bans_percent}</td>
        <td>${item.t_p_b}</td>
        <td>${item.percent_p_b}</td>
    `;
        dataHeroStats.appendChild(row);
    });
}

fetch('data/statistik_main_tournament.json') // Lokasi file JSON
    .then(response => {
        if (!response.ok) {
            throw new Error('Gagal mengambil data: ' + response.statusText);
        }
        return response.json();
    })
    .then(data => displayDataInTable(data))
    .catch(error => {
        console.error('Error:', error);
    });