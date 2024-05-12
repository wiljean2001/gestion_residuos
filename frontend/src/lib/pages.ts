import {
	Tag,
	Users,
	Settings,
	LayoutGrid,
	MapIcon,
	User2Icon,
	Trash2Icon,
	TruckIcon
} from "lucide-react"

type Submenu = {
	href: string
	label: string
	active: boolean
}

type Menu = {
	href: string
	label: string
	active: boolean
	icon: any
	submenus: Submenu[]
}

type Group = {
	groupLabel: string
	menus: Menu[]
}

export function getPages(pathname: string): Group[] {
	return [
		{
			groupLabel: "",
			menus: [
				{
					href: "/",
					label: "Dashboard",
					active: pathname.includes("/"),
					icon: LayoutGrid,
					submenus: []
				}
			]
		},
		// {
		// 	groupLabel: "Ubicaciones",
		// 	menus: [
		// 		{
		// 			href: "",
		// 			label: "Sedes",
		// 			active: pathname.includes("/posts"),
		// 			icon: MapIcon,
		// 			submenus: []
		// 		},
		// 		{
		// 			href: "",
		// 			label: "Almacenes",
		// 			active: pathname.includes("/posts"),
		// 			icon: MapIcon,
		// 			submenus: []
		// 		},
		// 		{
		// 			href: "",
		// 			label: "Personal",
		// 			active: pathname.includes("/posts"),
		// 			icon: MapIcon,
		// 			submenus: []
		// 		}
		// 	]
		// },
		{
			groupLabel: "",
			menus: [
				{
					href: "",
					label: "Ubicaciones",
					active: pathname.includes("/posts"),
					icon: MapIcon,
					submenus: [
						{
							href: "/posts",
							label: "Sedes",
							active: pathname === "/posts"
						},
						{
							href: "/posts",
							label: "Almacenes",
							active: pathname === "/posts"
						},
						{
							href: "/posts/new",
							label: "Personal",
							active: pathname === "/posts/new"
						}
					]
				},
				{
					href: "/categories",
					label: "Personal",
					active: pathname.includes("/categories"),
					icon: User2Icon,
					submenus: [
						{
							href: "/posts",
							label: "Conductores",
							active: pathname === "/posts"
						},
						{
							href: "/posts",
							label: "Supervisores",
							active: pathname === "/posts"
						},
						{
							href: "/posts/new",
							label: "Administradores",
							active: pathname === "/posts/new"
						}
					]
				},
				{
					href: "/tags",
					label: "Residuos",
					active: pathname.includes("/tags"),
					icon: Trash2Icon,
					submenus: [
						{
							href: "/posts",
							label: "Peligrosos",
							active: pathname === "/posts"
						},
						{
							href: "/posts",
							label: "No peligrosos",
							active: pathname === "/posts"
						},
						{
							href: "/posts/new",
							label: "RAEEs",
							active: pathname === "/posts/new"
						}
					]
				},
				{
					href: "/tags",
					label: "Recolecciones",
					active: pathname.includes("/tags"),
					icon: TruckIcon,
					submenus: [
						{
							href: "/posts",
							label: "Calendario",
							active: pathname === "/posts"
						},
						{
							href: "/posts",
							label: "Vehículos",
							active: pathname === "/posts"
						},
						{
							href: "/posts/new",
							label: "Rutas (¿?)",
							active: pathname === "/posts/new"
						}
					]
				}
			]
		},
		{
			groupLabel: "Reportes",
			menus: [
				{
					href: "/users",
					label: "Users",
					active: pathname.includes("/users"),
					icon: Users,
					submenus: []
				},
				{
					href: "/account",
					label: "Account",
					active: pathname.includes("/account"),
					icon: Settings,
					submenus: []
				}
			]
		}
	]
}
