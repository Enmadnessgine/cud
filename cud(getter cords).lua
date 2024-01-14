script_name("CUD (getter_coordinates)")
script_author("binoculars9 / alprazolam / Enmadnessgine")
script_version("1.0")
script_url("My GitHub: https://github.com/Enmadnessgine")

local socket = require("socket")


function main()
    while not isSampAvailable() do wait (100) end

    local websocketHost = "127.0.0.1"
	local websocketPort = 8000
	local websocketClient, err = connectToWebSocket(websocketHost, websocketPort)

	if websocketClient then
    	while true do
	        wait(3000)

	        local playerCoordinates = getPlayerCoordinates()
	        local sendResult = sendWebSocketData(websocketClient, playerCoordinates)

	        if sendResult then
	            print('Coordinates sent successfully')
	        else
	            print('Error sending coordinates')
	        end
    	end
	else
    print('Error connecting to WebSocket: ' .. err)
    end
    wait(-1)
end


function connectToWebSocket(host, port)
    local client = socket.tcp()
    client:settimeout(0)

    local _, err = client:connect(host, port)
    if err == 'timeout' then
        return client
    else
        return nil, err
    end
end


function sendWebSocketData(client, data)
    local _, err = client:send(data)
    return err
end


function getPlayerCoordinates()
    local x, y, z = getCharCoordinates(PLAYER_PED)
    return string.format('{"x":%f,"y":%f}', x, y)
end



