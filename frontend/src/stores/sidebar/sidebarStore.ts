// sidebarStore.js
import { useLocalStorageGet, useLocalStorageSave } from "@hooks/UseLocalStorage"
import { atom } from "nanostores"

// Crea un store atómico con el estado inicial
export const sidebar = atom({
	isOpen: useLocalStorageGet<boolean>("sidebar-open") || false
})

// Función para cambiar el estado
export const setSidebarOpen = () => {
	sidebar.set({ isOpen: !sidebar.get().isOpen })
	useLocalStorageSave<boolean>("sidebar-open", sidebar.get().isOpen)
}
