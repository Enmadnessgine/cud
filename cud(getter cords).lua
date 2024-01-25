script_name("CUD (getter_coordinates)")
script_author("binoculars9 / alprazolam. / Enmadnessgine")
script_version("1.0")
script_url("My GitHub: https://github.com/Enmadnessgine")

local ws = require("websocketsamp")

function main()
    if not isSampLoaded() or not isSampfuncsLoaded() then return end
    while not isSampAvailable() do wait(100) end

    ws.Connect("ws://127.0.0.1:8000/ws/player_coordinates/")
    sampRegisterChatCommand("scoords", scoords)
end

function scoords()
	local x, y, z = getCharCoordinates(PLAYER_PED)
	sampAddChatMessage("Your coordinates: X: " .. x .. " | Y:" .. y .. " | Z: " .. z, -1)
	local coordinates = {x = x, y = y}
    local json_data = encodeJson(coordinates)
	ws.SendMessage(json_data)
end

function onQuitGame()
    ws.Disconnect()
end
