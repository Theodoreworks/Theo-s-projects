const apiKey = "3bfd421c27c5962680bcc0739933c1cf";

const searchBtn = document.getElementById("searchBtn");
const searchInput = document.getElementById("searchInput");
const weatherResult = document.getElementById("weatherResult");

// Click search
searchBtn.addEventListener("click", () => {
    const city = searchInput.value.trim();

    if (city === "") {
        alert("Please enter a city");
        return;
    }

    getWeather(city);
});

// Press Enter to search (NEW)
searchInput.addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
        searchBtn.click();
    }
});

// MAIN WEATHER FUNCTION
async function getWeather(city) {
    try {
        // Loading state (NEW)
        weatherResult.innerHTML = `<p>Loading weather...</p>`;

        const response = await fetch(
            `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`
        );

        if (!response.ok) {
            throw new Error("City not found");
        }

        const data = await response.json();

        // Weather icon (NEW)
        const icon = data.weather[0].icon;
        const iconUrl = `https://openweathermap.org/img/wn/${icon}@2x.png`;

        weatherResult.innerHTML = `
            <h2>${data.name}</h2>
            <img src="${iconUrl}" alt="weather icon" />
            <p><strong>${data.main.temp}°C</strong></p>
            <p>${data.weather[0].description}</p>
            <p>Humidity: ${data.main.humidity}%</p>
        `;

    } catch (error) {
        weatherResult.innerHTML = `
            <p style="color:#ff6b6b;">
                City not found. Please try again.
            </p>
        `;
    }
}

// AUTO LOCATION ON LOAD (NEW BIG FEATURE)
window.addEventListener("load", () => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;

            getWeatherByCoords(lat, lon);
        });
    }
});

// WEATHER BY COORDINATES (NEW)
async function getWeatherByCoords(lat, lon) {
    try {
        const response = await fetch(
            `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}&units=metric`
        );

        const data = await response.json();

        const icon = data.weather[0].icon;
        const iconUrl = `https://openweathermap.org/img/wn/${icon}@2x.png`;

        weatherResult.innerHTML = `
            <h2>${data.name}</h2>
            <img src="${iconUrl}" alt="weather icon" />
            <p><strong>${data.main.temp}°C</strong></p>
            <p>${data.weather[0].description}</p>
            <p>Humidity: ${data.main.humidity}%</p>
        `;
    } catch (error) {
        console.log("Location weather error:", error);
    }
}