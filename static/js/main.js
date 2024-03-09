document.addEventListener('DOMContentLoaded', function() {
    // Initialize chart with data from API
    fetchChartData();
    
    // Set up event listener for the load winners button
    document.getElementById('loadWinners').addEventListener('click', fetchRandomWinners);
});

/**
 * Fetch data for the chart from the API
 */
function fetchChartData() {
    fetch('/api/winners-by-country')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Sort data by count (descending) and take top 15
            const sortedData = data.sort((a, b) => b.count - a.count).slice(0, 15);
            
            // Render chart with the data
            renderChart(sortedData);
        })
        .catch(error => {
            console.error('Error fetching chart data:', error);
        });
}

/**
 * Render a chart with the provided data
 */
function renderChart(data) {
    const ctx = document.getElementById('nobelChart').getContext('2d');
    
    // Extract labels and data
    const labels = data.map(item => item.country);
    const counts = data.map(item => item.count);
    
    // Generate vibrant colors
    const backgroundColors = generateColors(data.length);
    
    // Create chart
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Número de Ganadores',
                data: counts,
                backgroundColor: backgroundColors,
                borderColor: backgroundColors.map(color => color.replace('0.7', '1')),
                borderWidth: 2
            }]
        },
        options: {
            indexAxis: 'y',  // Create horizontal bar chart
            responsive: true,
            plugins: {
                legend: {
                    display: false,
                },
                title: {
                    display: true,
                    text: 'Premios Nobel por País (Top 15)',
                    font: {
                        family: 'Righteous',
                        size: 20
                    },
                    color: '#0f3460'
                }
            },
            scales: {
                x: {
                    grid: {
                        color: 'rgba(233, 69, 96, 0.2)'
                    },
                    ticks: {
                        font: {
                            family: 'Comfortaa',
                            weight: 'bold'
                        },
                        color: '#0f3460'
                    }
                },
                y: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        font: {
                            family: 'Comfortaa',
                            weight: 'bold'
                        },
                        color: '#0f3460'
                    }
                }
            }
        }
    });
}

/**
 * Generate an array of vibrant colors
 */
function generateColors(count) {
    const colors = [];
    for (let i = 0; i < count; i++) {
        // Use unusual color scheme
        const hue = (i * 137.5) % 360;  // Golden angle approximation for better distribution
        colors.push(`hsla(${hue}, 80%, 60%, 0.7)`);
    }
    return colors;
}

/**
 * Fetch random winners from the API
 */
function fetchRandomWinners() {
    // Show loading state
    const winnersList = document.getElementById('winners-list');
    winnersList.innerHTML = '<p class="loading">Cargando ganadores...</p>';
    
    fetch('/api/random-winners')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(winners => {
            displayWinners(winners);
        })
        .catch(error => {
            console.error('Error fetching random winners:', error);
            winnersList.innerHTML = '<p class="error">Error al cargar los ganadores. Por favor intente de nuevo.</p>';
        });
}

/**
 * Display winners in the DOM
 */
function displayWinners(winners) {
    const winnersList = document.getElementById('winners-list');
    
    // Clear previous content
    winnersList.innerHTML = '';
    
    // Add each winner to the DOM
    winners.forEach(winner => {
        const winnerCard = document.createElement('div');
        winnerCard.className = 'winner-card';
        
        winnerCard.innerHTML = `
            <h3>${winner.name}</h3>
            <p class="year">${winner.year}</p>
            <p class="category">Categoría: ${winner.category}</p>
            <p>País: ${winner.country || 'No especificado'}</p>
            ${winner.born_in ? `<p>Nacido en: ${winner.born_in}</p>` : ''}
        `;
        
        winnersList.appendChild(winnerCard);
    });
}
