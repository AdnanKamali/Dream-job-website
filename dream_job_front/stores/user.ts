import {defineStore} from "pinia";

export const useUserStore = defineStore({id: "user",
    state:() => ({
        user: {
            isAuthenticated: false,
            email: null as string | null,
            token: null as string | null,
        }
    }),

    actions: {
        initStore(){
            this.user.isAuthenticated = false;

            if(localStorage.getItem("user.token")){
                this.user.token = localStorage.getItem("user.token");
                this.user.email = localStorage.getItem("user.email");
                this.user.isAuthenticated = true;

                console.log("Intialized user: ", this.user);
            }
        },
        setToken(token: string, email: string){
            console.log("Set Token: ", token, email);

            this.user.token = token;
            this.user.email = email;
            this.user.isAuthenticated = true;
            
            localStorage.setItem("user.token", token);
            localStorage.setItem("user.email", email);
        },
        removeToken(){
            console.log("removeToken");

            this.user.token = null;
            this.user.email = null;
            this.user.isAuthenticated = false;
            
            localStorage.clear();
        }
    }
})