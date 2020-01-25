<template>
  <div>
    <v-app-bar flat height="100px">
      <v-toolbar-items class="items">
        <router-link to="/">
          <v-toolbar-title>
            <v-img class="brandImage" src="../assets/images/logo.png"></v-img>
          </v-toolbar-title>
        </router-link>
        <v-menu right  :open-on-hover="true">
          <template v-slot:activator="{ on }">
            <v-btn text v-on="on" class="btn">
              <b color:>Sobre Nós</b>
            </v-btn>
          </template>
          <v-list class="inline">
            <router-link to="/about">
            <v-list-item @click="() => {}">
            <v-list-item-title class="tab">
              <b>A Nossa História</b>
            </v-list-item-title>
            </v-list-item>
            </router-link>
            <router-link to="/team">
            <v-list-item >
            <v-list-item-title class="tab">
              <b>A Equipa</b>
              </v-list-item-title>
            </v-list-item>
            </router-link>
            <router-link to="/contact">
            <v-list-item >
            <v-list-item-title class="tab">
              <b>Contacte-nos</b>
             </v-list-item-title>
            </v-list-item>
            </router-link>
            <router-link to="/faq">
           <v-list-item>
            <v-list-item-title class="tab">
              <b>FAQs</b>
            </v-list-item-title>
            </v-list-item>
            </router-link>
          </v-list>
        </v-menu>
      </v-toolbar-items>
      <v-spacer></v-spacer>
      <v-toolbar-items class="items" v-if="!mobileView">
        <router-link to="/registo">
          <v-btn  text class="btn">
            <b>Registo</b>
          </v-btn>
        </router-link>
        <router-link to="/login">
          <v-btn text class="btn">
            <v-icon class="icon">fas fa-sign-in-alt</v-icon>
            <b>Iniciar Sessão</b>
          </v-btn>
        </router-link>
        <v-btn text @hidden="false" @click.stop="drawer = !drawer" class="btn">
          <v-icon class="icon">fas fa-user-circle</v-icon>
          <b>Área do Cliente</b>
        </v-btn>
      </v-toolbar-items>
      <v-toolbar-items class="items" v-if="mobileView">
        <v-btn text @hidden="true" @click.stop="drawer = !drawer" class="btn">
          <v-icon class="icon">fas fa-user-circle</v-icon>
          <b>Área do Cliente</b>
        </v-btn>
        <v-app-bar-nav-icon @click.stop="mobile = !mobile" class="responsiveicon"></v-app-bar-nav-icon>
      </v-toolbar-items>
    </v-app-bar>

    
      <v-navigation-drawer v-model="drawer" app temporary right width="300">
        <template v-slot:prepend>
          <v-list-item two-line>
            <v-list-item-avatar>
              <img src="https://randomuser.me/api/portraits/women/81.jpg" />
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title>Jane Smith</v-list-item-title>
              <v-list-item-subtitle>Logged In</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </template>
        <v-divider></v-divider>
        <v-list dense>
          <v-list-item v-for="item in items" :key="item.id">
            <v-list-item-content>
              <v-list-item-title>
                <router-link :to="`${item.page}`">
                  <v-btn text class="btn">
                    <v-icon>{{ item.icon }}</v-icon>
                    <span class="txt"><b>{{ item.title }}</b></span>
                  </v-btn>
                </router-link>
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <v-divider></v-divider>
        <v-btn text class="btn">
          <span class="txt"><b>Terminar Sessão</b></span>
          <v-icon class="icon">fas fa-sign-out-alt</v-icon>
        </v-btn>
      </v-navigation-drawer>

    <!-- responsive bar -->
    <v-navigation-drawer v-model="mobile" temporary app width="100%" height="50%" class="mobile">
      <v-list-item>
        <v-list-item-content>
          <v-row class="top-items">
            <router-link to="/">
              <v-img class="logo" src="../assets/images/logo.png"></v-img>
            </router-link>
            <v-spacer></v-spacer>
            <v-btn icon margin-right="30" @click.stop="mobile = !mobile" class="btn">
              <v-icon size="40px" class="responsiveicon">fas fa-times</v-icon>
            </v-btn>
          </v-row>

          <v-divider></v-divider>
          <router-link to="/registo">
            <v-btn text block class="btn">
              <b>Registo</b>
            </v-btn>
          </router-link>
          <v-divider></v-divider>
          <router-link to="/login">
            <v-btn text block class="btn">
              <v-icon class="icon">fas fa-sign-in-alt</v-icon>
              <b>Iniciar Sessão</b>
            </v-btn>
          </router-link>
          <v-divider></v-divider>
          <v-btn text block class="btn-drop">
            <b>Sobre Nós</b>
          </v-btn>
          <v-divider></v-divider>
        </v-list-item-content>
      </v-list-item>
      <v-row>
        <v-card-text>
          <v-btn v-for="icon in icons" :key="icon" class="mx-4 green--text" icon>
            <v-icon>{{ icon }}</v-icon>
          </v-btn>
        </v-card-text>
      </v-row>
      <v-card-text class="black--text">
        {{ new Date().getFullYear() }} —
        <strong>SpotNow</strong>
      </v-card-text>
    </v-navigation-drawer>
  </div>
</template>
  
<script>
export default {
  name: "Navigation",

  data() {
    return {
      drawer: false,
      mobile: false,
      mobileView: false,
      links: [
        {
          id: 0,
          text: "A nossa história",
          page: "/about"
        },
        {
          id: 1,
          text: "Contactos",
          page: "/contact"
        },
        {
          id: 2,
          text: "FAQs",
          page: "/faq"
        }
      ],
      items: [
        {
          id: 0,
          title: "Reservar Garagem",
          icon: "mdi-garage-open",
          page: "/reserva"
        },
        { id: 1, title: "Histórico", icon: "mdi-clipboard-list-outline", page: "/historico" },
        {
          id: 2,
          title: "Adicionar Garagem",
          icon: "mdi-garage",
          page: "/addgaragem"
        },
        {
          id: 3,
          title: "Notificações",
          icon: "mdi-bell",
          page: ""
        },
        {
          id: 4,
          title: "Métodos de Pagamento",
          icon: "mdi-credit-card-outline",
          page: "/payment"
        },
        {
          id: 4,
          title: "Dados da Conta",
          icon: "mdi-account-settings",
          page: "/settings"
        }
      ],
      icons: ["fab fa-facebook", "fab fa-twitter", "fab fa-google-plus"]
    };
  },
  methods: {
    handleView() {
      if (window.innerWidth <= 960) this.mobileView = true;
    }
  },

  created() {
    this.handleView();
  }
};
</script>

<style scoped>
.tab{
  align-items: center;
}

.items {
  margin-top: 20px;
  margin-bottom: 20px;
  align-items: center;
}

.btn {
  margin-left: 5px;
  align-items: center;
}

.icon {
  margin-right: 5px;
  margin-left: 2px;
  align-items: center;
}

.brandImage {
  background-size: 130px 100px;
  background-repeat: no-repeat;
  display: inline-block;
  margin-left: 50px;
  width: 130px;
  height: 100px;
}

.responsiveicon {
  padding: 10px 10px 20px;
  margin-left: 25px;
  margin-right: 30px;
  align-items: center;
  cursor: pointer;
  size: 40px;
}
.top-items {
  align-items: center;
}

.logo {
  background-size: 100px 60px;
  background-repeat: no-repeat;
  display: inline-block;
  margin-left: 100px;
  width: 130px;
  height: 60px;
}
</style> 