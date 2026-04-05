"""
MCP Client: Tích hợp gọi tool nội bộ qua Model Context Protocol
"""
class MCPClient:
    def __init__(self, server_url):
        self.server_url = server_url

    def call_tool(self, tool_name, payload):
        # TODO: Gửi request tới MCP server, nhận kết quả
        pass
