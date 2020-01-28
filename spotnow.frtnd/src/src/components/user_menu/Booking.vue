<template>
  <div>
    <!-- <v-card height="785px"> -->
    <!-- <v-navigation-drawer v-model="drawer" absolute expand-on-hover dark>
        <v-list dense nav class="py-0">
          <v-list-item two-line :class="miniVariant && 'px-0'">
            <v-list-item-content>
              <v-icon padding-top="15px" margin-left="15px" size="65px">mdi-map-search</v-icon>
              <v-list-item-title font-size="large">
                <b>Filtro de Procura</b>
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-divider></v-divider>
          <v-list-item>
            <div>
      <h2>Search and add a pin</h2>
      <label>
        <gmap-autocomplete
          @place_changed="setPlace">
        </gmap-autocomplete>
        <button @click="addMarker">Add</button>
      </label>
      <br/>
      </div>
          </v-list-item>
          <v-list-item>
            <label>
              <b>Mostrar X garagens</b>
            </label>
          </v-list-item>
          <v-list-item>
            <v-row>
              <label>
                <b>Preço inferior</b>
              </label>
            </v-row>
          </v-list-item>
          <v-list-item>
            <label>
              <gmap-autocomplete @place_changed="setPlace"></gmap-autocomplete>
              <button @click="addMarker">Add</button>
            </label>
          </v-list-item>
        </v-list>
    </v-navigation-drawer>-->

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
    <!-- </v-card> -->
  </div>
</template>

<script>
export default {
  name: "Booking",
  data: () => ({
    // default to Braga to keep it simple
    // change this to whatever makes sense
    center: { lat: 41.55032, lng: -8.42005 },
    markers: [
      {
        name: "Garagem SpotNow",
        description: ["Tipologia: Lugar de Garagem Individual","Preço: 5€"],
        date_build: "26-11-2019",
        position: { lat: 41.544707, lng: -8.425025 }
      }
    ],
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
    }
  }),
  mounted() {
    this.geolocate();
    // //set bounds of the map
    // this.$refs.gmap.$mapPromise.then(map => {
    //   const bounds = new google.maps.LatLngBounds();
    //   for (let m of this.markers) {
    //     bounds.extend(m.position);
    //   }
    //   map.fitBounds(bounds);
    // });
  },

  methods: {
    // receives a place object via the autocomplete component
    setPlace(place) {
      this.currentPlace = place;
    },
    addMarker() {
      if (this.currentPlace) {
        const marker = {
          lat: this.currentPlace.geometry.location.lat(),
          lng: this.currentPlace.geometry.location.lng(),
          infoText: this.currentPlace.name()
        };
        this.markers.push({ position: marker });
        this.places.push(this.currentPlace);
        this.center = marker;
        this.currentPlace = null;
      }
    },
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
      <time datetime="2016-1-1"><b>${marker.date_build}</b></time>
    </div>
    <br>
    <button><b>Reservar</b></button>
  </div>
</div>`);
      },
    }
};
</script>
<style>
.mapa {
  margin-left: 100px;
  margin-right: 100px;
  margin-bottom: 50px;
  justify-content: center;
  align-items: center;
}
</style>