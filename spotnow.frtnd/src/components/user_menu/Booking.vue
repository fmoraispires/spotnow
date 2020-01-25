<template>
  <div>
    <v-card height="785px">
      <v-navigation-drawer v-model="drawer" absolute dark>
        <v-list dense nav class="py-0">
          <v-list-item two-line :class="miniVariant && 'px-0'">
            <v-list-item-content>
              <v-icon padding-top="15px" margin-left="15px" size="65px">mdi-map-search</v-icon>
              <v-list-item-title font-size="large">
                <b>Filtro de Procura</b>
              </v-list-item-title>
              <!-- <v-list-item-subtitle> </v-list-item-subtitle> -->
            </v-list-item-content>
          </v-list-item>
          <v-divider></v-divider>
          <v-list-item>
              <label>
              <b>Escolha uma cidade</b>
              <gmap-autocomplete @place_changed="setPlace"></gmap-autocomplete>
              <button @click="addMarker">add</button>
              </label>
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
      </v-navigation-drawer>

      <gmap-map :center="center" :zoom="17" style="margin-left:250px; height:785px;">
        <gmap-info-window
          :options="infoOptions"
          :position="infoWindowPos"
          :opened="infoWinOpen"
          @closeclick="infoWinOpen=false"
        >
          <button type="button" style="background-color: pink;">Hello!</button>
          <ul>
            <li>List Item</li>
            <li>Another One</li>
          </ul>
        </gmap-info-window>
        <gmap-marker
          :key="index"
          v-for="(m, index) in markers"
          :position="m.position"
          :icon="{url: require('../../assets/images/marker.png'),scaledSize: {width: 80, height: 80}}"
        ></gmap-marker>
      </gmap-map>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "Booking",
  data: () => ({
    // default to Braga to keep it simple
    // change this to whatever makes sense
    center: { lat: 41.55032, lng: -8.42005 },
    markers: [],
    places: [],
    currentPlace: null,
    infoContent: "",
    infoWindowPos: null,
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
    toggleInfoWindow: function(marker, idx) {
      this.infoWindowPos = marker.position;
      this.infoContent = marker.infoText;

      //check if its the same marker that was selected if yes toggle
      if (this.currentMidx == idx) {
        this.infoWinOpen = !this.infoWinOpen;
      }
      //if different marker set infowindow to open and reset current marker index
      else {
        this.infoWinOpen = true;
        this.currentMidx = idx;
      }
    }
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