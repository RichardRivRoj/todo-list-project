"use client";
import { useEffect } from "react";

import { useAuthStore } from "@/store/authStore";

export default function DashboardPage() {
  const user = useAuthStore((state) => state.user);

  useEffect(() => {
    if (!user) window.location.href = "/login"; // Redirigir si no está autenticado
    fetchTasks();
  }, []);

  return (
    <div>
      <h1>Tus Tareas</h1>
      {/* Listar tareas */}
    </div>
  );
}