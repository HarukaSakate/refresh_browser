require 'curb'

loop do
  begin
    response = Curl.get("https://example.com") #任意のURLを設定する
    if response.status.include?("200")
      puts "Page reloaded"
    else
      puts "Failed to reload page: #{response.status}"
    end
  rescue Curl::Err::CurlError => e
    puts "Curl error: #{e.message}"
  end

  # スリープ時間
  sleep(300)
end
