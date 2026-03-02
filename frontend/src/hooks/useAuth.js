import { useEffect, useState } from "react";
import { api } from "../api/client";

export function useAuth() {
  const [state, setState] = useState({ loading: true, authenticated: false, user: null });

  useEffect(() => {
    api.me()
      .then((data) => {
        if (data && data.authenticated) {
          setState({ loading: false, authenticated: true, user: data.user });
        } else {
          window.location.href = "/auth/login";
        }
      })
      .catch(() => {
        window.location.href = "/auth/login";
      });
  }, []);

  const logout = async () => {
    await api.logout();
    window.location.href = "/auth/login";
  };

  return { ...state, logout };
}
