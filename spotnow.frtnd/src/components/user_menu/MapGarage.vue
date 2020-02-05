<template>
  <div>
    <gmap-map :center="center" :zoom="17" style="width:100%; height:785px;">
      <gmap-marker
        :key="index"
        v-for="(m, index) in markers"
        :position="m.position"
        @click="toggleInfoWindow(m,index)"
        :icon="{url: require('../../assets/images/marker.png'),scaledSize: {width: 80, height: 80}}"
      ></gmap-marker>
      <gmap-info-window
        :options="infoOptions"
        :position="infoWindowPos"
        :opened="infoWinOpen"
        @closeclick="infoWinOpen=false"
      >
        <div v-html="infoContent"></div>
      </gmap-info-window>
    </gmap-map>
   <!-- <ul>
      Garage:
      <br>
      ID:
        <li v-for="garage in garages" v-bind:key="garage" v-text="garage.id"></li>
      Nome:
      <li v-for="garage in garages" v-bind:key="garage" v-text="garage.name"></li>
      Morada:
      <li v-for="garage in garages" v-bind:key="garage" v-text="garage.address"></li>
   </ul>
   <ul> 
       Markers:
      <br>
      Nome:
      <li v-for="marker in markers" v-bind:key="marker" v-text="marker.name"></li>

    </ul>


    <v-btn @click="fillMarkers"></v-btn> -->
  </div>
</template>

<script>
export default {
  name: "MapGarage",
  data: () => ({
    // default to Braga to keep it simple
    // change this to whatever makes sense
    center: { lat: 41.55032, lng: -8.42005 },
    garages:null,
    markers: [ {
            name: "Garagem 1",
            description:["Tipologia: Lugar de Garagem Individual","Preço: 5€","Morada: Rua Nova Santa Cruz","reserva"],
            date_build: "",
            position: {lat: 41.556049, lng: -8.401903}
          },
          {
            name: "Garagem 2",
            description: ["Tipologia: Lugar de Garagem Individual","Preço: 5€","Morada: Rua Jose Maria Ottoni","reserva2"],
            date_build: "",
            position: {lat: 41.554159, lng: -8.396568}
          },
          {
            name: "Garagem 3",
            description: ["Tipologia: Lugar de Garagem Individual","Preço: 5€","Morada: Rua Nova Santa Cruz","reserva3"],
            date_build: "",
            position: {lat: 41.557919, lng: -8.406017}
          },],
    places: [],
    infoContent: "",
    infoWindowPos: {
      lat: 0,
      lng: 0
    },
    infoWinOpen: false,
    currentMidx: null,
    //optional: offset infowindow so it visually sits nicely on top of our marker
    infoOptions: {
      pixelOffset: {
        width: 0,
        height: -35
      }
    },
  }),
  mounted() {
    this.geolocate();
    this.getGarage();
    this.fillMarkers();
  },

  methods: {
      /* eslint-disable no-console */

    getGarage(){
      this.$http
      .get("http://spotnow.westeurope.cloudapp.azure.com:8000/api/garages/")
      .then(response => (this.garages = response.data));
      // .finally(() => console.log("Morada:"+ this.garages[5].address +", "+this.garages[5].city +"\n"))
      
      
    },
  

    fillMarkers(){
        var i;
        var morada;
        
        
        for(i = 0; i < this.garages.length; i++){

          if(this.garages[i].name != null){
             morada = this.garages[i].address +", "+this.garages[i].city +"\n"
            
            var name = this.garages[i].name
            var descrip = ["Tipologia: Lugar de Garagem Individual","Preço: "+this.garages[i].preco,"Morada: "+morada, "Dono: "+this.garages[i].owner]
            var date = this.garages[i].createddate

            this.markers[i] = [{
                  name: name,
                  description: descrip,
                  date_build: date,
                  position: { lat: 41.555992, lng:  -8.401924}
                },]
            }
        }
    },
    /* eslint-enable no-console */

    geolocate: function() {
      navigator.geolocation.getCurrentPosition(position => {
          this.center = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
      });
    },
    toggleInfoWindow: function (marker, idx) {
        this.infoWindowPos = marker.position;
        this.infoContent = this.getInfoWindowContent(marker);
        

        //check if its the same marker that was selected if yes toggle
        if (this.currentMidx == idx) {
          this.infoWinOpen = !this.infoWinOpen;
        }
        //if different marker set infowindow to open and reset current marker index
        else {
          this.infoWinOpen = true;
          this.currentMidx = idx;
        }
      },
    getInfoWindowContent: function (marker) {
        return (`<div class="card">
                <div class="card-image">
                  <figure class="image is-4by3">
                    <img src="https://cdn.vente-unique.com/thumbnails/rs/230/337/337577/0/garagem_337577.png" alt="Placeholder image">
                  </figure>
                </div>
                <div class="card-content">
                  <div class="media">
                    <div class="media-content">
                      <p class="title is-4"><b>${marker.name}</b></p>
                    </div>
                  </div>
                  <div class="content">
                    <b>${marker.description[0]}</b>
                    <br>
                    <b>${marker.description[1]}</b>
                    <br>
                    <b>${marker.description[2]}</b>
                    <br>
                  </div>
                  <br>
                  <a href="http://spotnow.westeurope.cloudapp.azure.com:8080/#/${marker.description[3]}"><b>Reservar</b></a>
                </div>
              </div>`);
          },
        }
    };
</script>
<style>
.mapa {
  margin-top: 250px;
  margin-left: 100px;
  margin-right: 100px;
  margin-bottom: 50px;
  justify-content: center;
  align-items: center;
}
</style>