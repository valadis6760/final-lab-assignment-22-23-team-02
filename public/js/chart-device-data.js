/* eslint-disable max-classes-per-file */
/* eslint-disable no-restricted-globals */
/* eslint-disable no-undef */
$(document).ready(() => {
  console.log("document_ready");

  let maxLenght = 11;
  let humidityData = new Array(maxLenght);
  let pressureData = new Array(maxLenght);
  let temperatureData = new Array(maxLenght);
  let dronebatteryData = new Array(maxLenght);

  function updateDevice(id, time, date, temp, bat) {
    document.getElementById(id + "_time").textContent = time;
    document.getElementById(id + "_date").textContent = date;
    document.getElementById(id + "_temp").textContent = temp;
    document.getElementById(id + "_batt").textContent = bat;
  }

  function getAverage(array) {
    const sum = array.reduce(
      (accumulator, currentValue) => accumulator + currentValue
    );
    return Math.round(sum / array.length, 1);
  }

  function getPercent(array) {
    const onesCount = array.filter((element) => element === 1).length;
    return (onesCount / array.length) * 100;
  }

  function getHealth(array) {
    return array.map((element) => {
      if (element > 35) {
        return 0;
      } else {
        return 1;
      }
    });
  }

  function getBattery(array) {
    return array.map((element) => {
      if (element < 20) {
        return 0;
      } else {
        return 1;
      }
    });
  }

  var drone_bat_ctx = document
    .getElementById("drone-battery-chart")
    .getContext("2d");

  // Create the data for the chart
  var droneBatData = {
    labels: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    datasets: [
      {
        label: "Discharge (%)",
        borderColor: "blue",
        fill: false,
      },
    ],
  };

  // Create the options for the chart
  var droneBatOptions = {
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: true,
          },
        },
      ],
    },
  };

  // Create the chart
  var droneBatChart = new Chart(drone_bat_ctx, {
    type: "line",
    data: droneBatData,
    options: droneBatOptions,
  });

  var weather_ctx = document.getElementById("weather-chart").getContext("2d");

  var weatherData = {
    labels: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    datasets: [
      {
        label: "Temperature (°C)",
        borderColor: "yellow",
        fill: false,
      },
      {
        label: "Humidity (%)",
        borderColor: "red",
        fill: false,
      },
      {
        label: "Pressure (kPa)",
        borderColor: "green",
        fill: false,
      },
    ],
  };

  var weatherOptions = {
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: true,
          },
        },
      ],
    },
  };

  var weatherChart = new Chart(weather_ctx, {
    type: "line",
    data: weatherData,
    options: weatherOptions,
  });

  function addData(temp, humd, press, batt) {
    humidityData.push(humd);
    pressureData.push(press);
    temperatureData.push(temp);
    dronebatteryData.push(batt);

    if (humidityData.length > maxLenght) {
      humidityData.shift();
      pressureData.shift();
      temperatureData.shift();
      dronebatteryData.shift();
    }
  }

  const protocol = document.location.protocol.startsWith("https")
    ? "wss://"
    : "ws://";
  const webSocket = new WebSocket(protocol + location.host);

  // When a web socket message arrives:
  // 1. Unpack it
  // 2. Validate it has date/time and temperature
  // 3. Find or create a cached device to hold the telemetry data
  // 4. Append the telemetry data
  // 5. Update the chart UI
  webSocket.onmessage = function onMessage(message) {
    try {
      const recivedData = JSON.parse(message.data);
      const messageData = recivedData.IotData;
      console.log(messageData);

      // Temperature, Humidity & Pressure

      document.getElementById("temp").textContent =
        messageData.edge_device.temperature;
      document.getElementById("humd").textContent =
        messageData.edge_device.humidity;
      document.getElementById("press").textContent =
        messageData.edge_device.pressure;

      // Adding Data to Weather chart and Battery Chart

      addData(
        messageData.edge_device.temperature,
        messageData.edge_device.humidity,
        messageData.edge_device.pressure,
        messageData.edge_device.battery
      );
      weatherData.datasets[0].data = humidityData;
      weatherData.datasets[1].data = pressureData;
      weatherData.datasets[2].data = temperatureData;
      droneBatData.datasets[0].data = dronebatteryData;
      droneBatChart.update();
      weatherChart.update();

      // Chart statistics - weather

      document.getElementById("avg_hum").textContent = getAverage(humidityData);
      document.getElementById("avg_press").textContent =
        getAverage(pressureData);
      document.getElementById("avg_temp").textContent =
        getAverage(temperatureData);

      document.getElementById("avg_hum_pgs").style.width =
        getAverage(humidityData) + "%";
      document.getElementById("avg_press_pgs").style.width =
        getAverage(pressureData) + "%";
      document.getElementById("avg_temp_pgs").style.width =
        getAverage(temperatureData) + "%";

      // Chart statistics - battery

      document.getElementById("drone_bat_percent").textContent =
        messageData.edge_device.battery;
      document.getElementById("drone_bat_percent_pgs").style.width =
        messageData.edge_device.battery + "%";

      // Farm Statistics

      var myAnimalBattery = [];
      var myAnimalHealth = [];
      var collar_data = messageData.devices;
      var timeStamp = messageData.ts;
      const dateObject = new Date(timeStamp * 1000);
      const read_date = dateObject.toLocaleDateString("pt-PT");
      const read_time = dateObject.toLocaleTimeString();
      // update Active Livestock Table
      collar_data.map((x) => {
        console.log(x);
        myAnimalHealth.push(x.temperature);
        myAnimalBattery.push(x.battery);
        updateDevice(x.id + 1, read_time, read_date, x.temperature, x.battery);
      });

      document.getElementById("farm_total").textContent =
        messageData.devices.length;

      document.getElementById("farm_batt").textContent = getPercent(
        getBattery(myAnimalBattery)
      );

      document.getElementById("farm_health").textContent = getPercent(
        getHealth(myAnimalHealth)
      );
    } catch (err) {
      console.error(err);
    }
  };
});
